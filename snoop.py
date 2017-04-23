# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:07:37 2017

@author: noner_000
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
   return "Under construction"

if __name__ == '__main__':
    app.run(port=5000, debug=True)