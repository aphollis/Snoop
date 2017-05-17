# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:07:37 2017

@author: noner_000
"""

from flask import Flask
from flask import render_templates

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)