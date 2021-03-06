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
import dosomething as ds
import sys

app = Flask(__name__)
date_time=str(datetime.datetime.now())

@app.route("/", methods=['GET', 'POST'])
def home():
    """Core function that generates pages and handles server manipulation"""
    sys.stderr.write('Print is working.\n')
    sys.stderr.write(str(request))
    sys.stderr.write('\n')
    sys.stderr.write(str(request.form.items()))
    sys.stderr.write('\n')

    if request.method == 'POST':

        formget = request.form.get('submit')
        sys.stderr.write('Formget = ' + str(formget)+'\n')

        #get input of button
        if formget is None:
            user_select_vpn = request.form.get('user_select_vpn')
            sys.stderr.write('user_select_vpn = ' + str(user_select_vpn) + '\n')
            ds.server_select(user_select_vpn)
            # restart server
            ds.startstop('restart')
        elif formget in ['Start', 'Stop', 'Restart']:
            #pass to startstop function

            sys.stderr.write('Startstop = ' + str(formget) + '\n')
            ds.startstop(formget)

        
        # #get input of dropdown to select new server
        # user_select_vpn = request.form.get('user_select_vpn')
        # if user_select_vpn == None:
        #     pass
        # elif len(user_select_vpn) > 0:
        #     #change server
        #     ds.server_select(user_select_vpn)
        #     #restart server
        #     ds.startstop('restart')
        #
        # #do this when nothing is there
        # else:
        #     pass
    
    #package everything up and render
    resp = make_response(render_template("home.html",
                          vpn_status=get_current_vpn_status(),
                          available_vpn=ds.available_servers(),
                          current_vpn=ds.get_current_server(),
                          action=next_action(),
                          date_time=date_time))
    return resp

#@app.route("/error")
#def InputError(value):
#    ##TODO generate nice error page    
#    return render_template("error.html",
#                           value=value,
#                           datetime=datetime,
#                           available_vpn=get_available_vpn(),
#                           current_vpn=get_current_vpn(),
#                           vpn_status=get_current_vpn_status())

def get_current_vpn_status():
    """Returns human readable string with status of VPN"""
    
    vpnstatus = ds.status()
    if vpnstatus == True:
        vpnstatus = 'Connected'
    elif vpnstatus == False:
        vpnstatus = 'Not Connected'
    else:
        vpnstatus = 'Error?'
    return vpnstatus

def next_action():
    """Returns string with next availabe action based upon server's current status"""
    
    if ds.status()==True:
        return "Stop"
    else:
        return "Start"

if __name__ == '__main__':
    app.run(debug=True)