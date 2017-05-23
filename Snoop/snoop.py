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
from dosomething import status

app = Flask(__name__)
date_time=str(datetime.datetime.now())

@app.route("/")
def home():
    ##bundle up response into object
    resp = make_response(render_template("home.html",
                          status=status,
                          vpn=get_available_vpn(),
                          current_vpn=get_current_vpn(),
                          date_time=date_time))
    #set cookie expiration
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    #set cookie for status

    return resp


def get_vpncity():
    #gets the user selected server from the page
    query = request.args.get("vpncity")
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

def get_available_vpn():
    ## TODO make this a parameter that's user definable
    resp = requests.get('https://www.privateinternetaccess.com/pages/client-support/')
    page = BeautifulSoup(resp.text, "html.parser")
    ## precess page for list of servers
    
    ##TESTING ONLY
    available = ['us-newyorkcity.privateinternetaccess.com',
                 'us-texas.privateinternetaccess.com',
                 'us-midwest.privateinternetaccess.com']
    return available #list conatining server names

def get_current_vpn():
    ## TODO make this function get name of currently connected vpn server
    
    ##TESTING ONLY
    current = 'us-newyorkcity.privateinternetaccess.com'
    return current #string conatining name of server. return empty string if
                    #no connection

def get_current_vpn_status():
    
    if status() == True:
        status = 'Connected'
    else:
        status = 'Not Connected'
    return status

if __name__ == '__main__':
    app.run(debug=True)