# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:44:35 2016

@author: fred
"""
import subprocess

from flask import Flask
from flask import request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import sys

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/buy')
@payment.required(3000)
def buy_fortune():

    fortune = subprocess.check_output(['fortune', 'riddles'])
    return fortune

# Initialize and run the server
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5005, debug=True)