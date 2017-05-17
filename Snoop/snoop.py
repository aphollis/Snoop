#!/usr/local/bin/python3
"""
Created on Sat Apr 22 17:07:37 2017

@author: noner_000
"""

from flask import Flask
from flask import render_template
from flask import request
import datetime

app = Flask(__name__)
datetime=str(datetime.datetime.now())

@app.route("/")
def home():
   return render_template("home.html",
                          status="REPLACE WITH STATUS AS STRING",
                          datetime=datetime)


def get_vpncity():
    query = request.args.get("vpncity")
    try:
        available.index(query)
    except ValueError as v:
        raise InputError(query)

@app.route("/error")
def InputError(value):
       return render_template("error.html", value=value, datetime=datetime)

def get_availablevpncity():
    # TODO: write function that finds available cities from VPN provider
    # returns as list of text string
    return available


if __name__ == '__main__':
    app.run(debug=True)