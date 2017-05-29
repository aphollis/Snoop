"""Various functions for executing terminal commands via browser interface
"""
import subprocess
import requests
from time import sleep
from bs4 import BeautifulSoup as bs
import fileinput
"""el button starts, stops, and outputs status of the vpn server
   actions are start, stop, status.
   locale is the server locale, and should probably come from a VPN web source
"""

"""
 Change locale based on list of server locations, this will have to read and write to a file to reset the openvpn locale files, unless all server locations can be set up in the openvpn Dir.

Alerts will need to write to a config file to store info.  what else does our config need?


"""

# def el_button():
#
#     #if openvpn is running, stop process, else, start process
#
#     if status() == True:
#         startstop('stop', 'Seattle')
#
#     elif status() == False:
#         startstop('start', 'Seattle')

def startstop(action):
    """Starts or stops the Pi VPN process. Takes linux systemctl action"""
    #use subprocess lib to start/stop openvpn, wait for command to complete, print status

    command = subprocess.Popen(['sudo', 'systemctl', action.lower(), 'openvpn@snoop'])
    command.wait()
    #print("New OpenVPN Status: " + str(status()))

def status():
    """Return's current status of the VPN server as Bool."""
    #output running processes and attempt to find openvpn process.

    output = subprocess.check_output(('ps', '-A'))
    state = output.find('openvpn')

    if state == -1:
        running = False
    else:
        running = True

    return running

#Parse PIA Host website and return dict w/ Host name and host address
def available_servers():
    """Returns dictionary of server locales with hostnames.
    Pulled from privateinternet's current website."""
    page = requests.get('https://www.privateinternetaccess.com/pages/network/')

    #TODO insert better error handling here...
    while page.status_code != 200:
        sleep(2)
        page
    else:
        soup = bs(page.content, 'html.parser')
        server_parser = soup.find_all('td', attrs={"data-label":"Hostname"})

        server_dict = dict()

        for item in server_parser:
            key = item.find_next_sibling('td').text.strip()

            for string in item.stripped_strings:
                value = string

                server_dict.update({key: value})

        return server_dict

def server_select(locale):
    read_conf = open('/etc/openvpn/snoop.conf', 'r')
    lines = read_conf.readlines()

    write_conf = open('/etc/openvpn/snoop.conf', 'w+')

    server = available_servers()
    server = server.get(locale)
    findit = 'privateinternetaccess.com'
    conf_line = 'remote ' + server + ' 1198\n'



    # for line in fileinput.FileInput(config, inplace=1):
    #     if findit in line:
    #         line.replace(findit, conf_line)

    for i, line in enumerate(lines):
        if findit in line:
            lines[i] = conf_line

    read_conf.close()

    write_conf.writelines(lines)

    write_conf.close()

def get_current_server():
    pass
    available = dict(available_servers())
    all_servers = available.values()
    read_conf = open('/etc/openvpn/snoop.conf', 'r')
    lines = read_conf.readlines()
    key_by_value = {v: k for k, v in available_servers.iteritems()}

    while status():
        for i, line in enumerate(lines):
            for item in all_servers:
                if item in line:
                    server = key_by_value.get(item)

    else:
        server = u'Snoop is not connected to a server'

    print(server)
    return server

    read_conf.close()




def iptables():
    pass

def alerts():
    pass

if __name__ == "__main__":

    get_current_server()

