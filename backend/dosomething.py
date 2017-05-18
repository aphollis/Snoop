"""Various functions for executing terminal commands via browser interface
"""
import subprocess
from time import sleep

"""el button starts, stops, and outputs status of the vpn server
   actions are start, stop, status.
   locale is the server locale, and should probably come from a VPN web source
"""

"""TODO: 
Check if process is running in el_button, process status is used to determine 'action' var (start/stop/etc.)
 
Change locale based on list of server locations, this will have to read and write to a file to reset the openvpn locale files, unless all server locations can be set up in the openvpn Dir.

Alerts will need to write to a config file to store info.  what else does our config need?


"""


def el_button(locale):

    #if openvpn is running, stop process, else, start process

    if status() == True:
        subprocess.Popen(['sudo', 'systemctl', 'stop', 'openvpn@' + locale])
        sleep(2)
        print("New OpenVPN Status: " + str(status()))


    elif status() == False:
        subprocess.Popen(['sudo', 'systemctl', 'start', 'openvpn@' + locale])
        sleep(2)
        print("New OpenVPN Status: " + str(status()))


def status():
    #output running processes and attempt to find openvpn process.
    output = subprocess.check_output(('ps', '-A'))
    state = output.find('openvpn')

    if state == -1:
        running = False
    else:
        running = True

    return running


def bypass():
    pass

def alerts():
    pass

if __name__ == "__main__":

    print('OpenVPN Status: ' + str(status()))

    el_button('Seattle')
