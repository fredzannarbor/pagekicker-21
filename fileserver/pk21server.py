#!/usr/bin/env python3
import os
import sys
import json
import random
import os.path

from flask import Flask
from flask import request
from flask import send_from_directory

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# machine-payable endpoint that returns fortune if payment made
@app.route('/buy')
@payment.required(1000)
def buy_fortune():

    fortune = subprocess.check_output(["fortune"])
    print(fortune)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
