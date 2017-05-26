"""Various functions for executing terminal commands via browser interface
"""
import subprocess
import os.path
import requests
from time import sleep
from bs4 import BeautifulSoup as bs
"""el button starts, stops, and outputs status of the vpn server
   actions are start, stop, status.
   locale is the server locale, and should probably come from a VPN web source
"""

"""
 Change locale based on list of server locations, this will have to read and write to a file to reset the openvpn locale files, unless all server locations can be set up in the openvpn Dir.

Alerts will need to write to a config file to store info.  what else does our config need?


"""

def el_button():

    #if openvpn is running, stop process, else, start process

    if status() == True:
        startstop('stop', 'Seattle')

    elif status() == False:
        startstop('start', 'Seattle')

def startstop(action, locale):

    #use subprocess lib to start/stop openvpn, wait for command to complete, print status

    command = subprocess.Popen(['sudo', 'systemctl', action, 'openvpn@snoop'])
    command.wait()
    #print("New OpenVPN Status: " + str(status()))
    server_select(locale)

def status():

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
    config = open('c:/etc/openvpn/snoop.conf', 'w')
    lines = config.readlines()
    server = available_servers()
    server = server('locale')
    conf_line = 'remote ' + server + ' 1198'


    for line in lines:
        if 'privateinternetaccess.com' in line:
            current = line
            line.replace(current, conf_line)
        else: line = line

    config.writelines()

    config.close()


def active_server():
    pass
    """AH - I need to build a script that will alter the vpn config file and then restart the server. once that is implemented the current server can be checked in /var/run/openvpn.  this is the most straightforward way i can find to check the actual server name/location.  Now that the scraper for the server list is done, i can work on this part next."""


def iptables():
    pass

def alerts():
    pass

if __name__ == "__main__":

    #print('OpenVPN Status: ' + str(status()))
    print(available_servers().keys())
    #el_button()
    locale = input('Select a server: ')
    server_select(locale)
