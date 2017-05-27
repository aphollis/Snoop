#!/usr/local/bin/python3
"""
Created on Sat Apr 22 17:07:37 2017

@author: noner_000
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import requests
from bs4 import BeautifulSoup 
import datetime
from dosomething import status, available_servers

app = Flask(__name__)
date_time=str(datetime.datetime.now())

@app.route("/", method=['GET', 'POST'])
def home():
    #get what user submitted
    user_select_vpn = request.form.get("user_select_vpn")
    
    #do this if something is there
    if len(user_select_vpn) > 0:
        ### set new VPN; restart server
        pass
        # If restart fails, send to error page
    
    #do this when nothing is there    
    else:
        pass
    
    resp = make_response(render_template("home.html",
                          vpn_status=get_current_vpn_status(),
                          available_vpn=available_servers(),
                          current_vpn=get_current_vpn(),
                          action=next_action(),
                          date_time=date_time))
    return resp

def get_vpncity():
    #gets the user selected server from the page
    query = request.form.get("vpncity")
    try:
        return get_available_vpn().index(query)

    except ValueError as v:
        raise InputError(query)

@app.route("/error")
def InputError(value):
    ##TODO generate nice error page    
    return render_template("error.html",
                           value=value,
                           datetime=datetime,
                           available_vpn=get_available_vpn(),
                           current_vpn=get_current_vpn(),
                           vpn_status=get_current_vpn_status())

def set_current_vpn():

    """AH - I need to build a script that will alter the vpn config file and then restart the server. once that is implemented the current server can be checked in /var/run/openvpn.  this is the most straightforward way i can find to check the actual server name/location.  Now that the scraper for the server list is done, i can work on this part next."""
   
    return set_report ##return TRUE, worked; FALSE, didn't work


def get_current_vpn():
    ## TODO make this function get name of currently connected vpn server

    """need to build a script that will read the current vpn server."""
    
    ##TESTING ONLY
    current = 'us-newyorkcity.privateinternetaccess.com'
    return current #string conatining name of server. return empty string if
                    #no connection

def get_current_vpn_status():
    vpnstatus = status()
    if vpnstatus == True:
        vpnstatus = 'Connected'
    else:
        vpnstatus = 'Not Connected'
    return vpnstatus

def next_action():
    if status()==True:
        return "Stop"
    else:
        return "Start"

if __name__ == '__main__':
    app.run(debug=True)