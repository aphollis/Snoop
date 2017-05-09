"""Various functions for executing terminal commands via browser interface
"""
import subprocess

"""el button starts, stops, and outputs status of the vpn server
   actions are start, stop, status.
   locale is the server locale, and should probably come from a VPN web source
"""
def el_button(action, locale)
    push=subprocess.run(['sudo', 'systemctl', action, 'openvpn@', locale])

def bypass():
    pass

def alerts():
    pass
