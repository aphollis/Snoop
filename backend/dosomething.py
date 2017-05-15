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
def el_button(action, locale):
    push=subprocess.Popen(['sudo', 'systemctl', action, 'openvpn@' + locale], stdout=subprocess.PIPE)
    status=subprocess.check_output(('push', '-A'))
    checkstate = status.find('(running)')

    if checkstate == True:
        print('OpenVPN is running')
    else: print('OpenVPN is not running')

def bypass():
    pass

def alerts():
    pass

if __name__ == "__main__":

    el_button('status', 'Seattle')