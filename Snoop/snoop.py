#!/usr/local/bin/python3
"""
Created on Sat Apr 22 17:07:37 2017

@author: noner_000
"""

from flask import Flask
from flask import render_template
from flask import request
import requests
from bs4 import BeautifulSoup 
import datetime

app = Flask(__name__)
datetime=str(datetime.datetime.now())

@app.route("/")
def home():
    response = make_response()
    return render_template("home.html",
                          status="REPLACE WITH STATUS AS STRING",
                          datetime=datetime)


def get_vpncity():
    #gets the user selected server from teh pag
    query = request.args.get("vpncity")
    try:
        available.index(query)
    except ValueError as v:
        raise InputError(query)

@app.route("/error")
def InputError(value):
    ##TODO generate nice error page    
    return render_template("error.html",
                           value=value,
                           datetime=datetime,
                           availablevpn=get_available_vpn(),
                           current_vpn=get_current_vpn())

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

if __name__ == '__main__':
    app.run(debug=True)