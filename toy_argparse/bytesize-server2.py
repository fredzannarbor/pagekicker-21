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

#@app.route('/fortune')
#@payment.required(3000)

def fortune(fortunefile1):

    #fortunefile1 = str(request.args.get('fortunefile1'))
    #fortunefile2 = str(request.args.get('fortunefile2'))
    result = subprocess.check_output(['fortune', fortunefile1]).decode('utf-8')
    print(result)
    return fortune

# Initialize and run the server
if __name__ == '__main__':
    fortunefile1 = sys.argv[1]
    fortunefile2 = sys.argv[2]
    fortune(fortunefile1)

    app.run(host='0.0.0.0', port=5005, debug=True)