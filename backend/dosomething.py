"""Various functions for executing terminal commands via browser interface
"""
import subprocess

"""el button starts, stops, and outputs status of the vpn server
   actions are start, stop, status.
   locale is the server locale, and should probably come from a VPN web source
"""

"""TODO: 
Check if process is running in el_button, process status is used to determine 'action' var (start/stop/etc.)
 
Change locale based on list of server locations, this will have to read and write to a file to reset the openvpn locale files, unless all server locations can be set up in the openvpn Dir.

Alerts will need to write to a config file to store info.  what else does our config need?


"""


def el_button(locale, action, recurse=True):
    subprocess.Popen(['sudo', 'systemctl', action, 'openvpn@' + locale], stdout=subprocess.PIPE)
    running = status()

    #if openvpn is running, stop process, else, start process

    while running and recurse:
        el_button(locale, 'stop', False)

    while not running and recurse:
        el_button(locale, 'start', False)

    print('OpenVPN Running: ' + str(status()))


def status():
    #output running processes and attempt to find openvpn process.
    output = subprocess.check_output(('ps', '-A'))
    status = output.find('openvpn')

    if status == -1:
        running = False
    else: running = True

    return running


def bypass():
    pass

def alerts():
    pass

if __name__ == "__main__":

    print('OpenVPN Status: ' + str(status()))
    whatdo = str(input('What do you want to do? start, stop: '))
    whatdo = whatdo.lower()

    el_button('Seattle', whatdo)
