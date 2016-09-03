#!/usr/bin/env python3

import subprocess
import yaml
import json
from flask import Flask, request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# machine-payable endpoint
@app.route('/buy')
@payment.required(2750)

def buy_yoda():

    sentence = request.args.get('sentence')
    yoda = subprocess.check_output(['perl', 'yoda2.pl', sentence])
    return yoda

@app.route('/manifest')
def docs():
    '''
    Serves the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

