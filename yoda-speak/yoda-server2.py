#!/usr/bin/env python3

import os
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

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")
    def run(daemon):
        if daemon:
            pid_file = './yoda.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'yoda-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting yoda-server.py daemon")
        else:
            print("Server running...")
            app.run(host='::', port=5001)

    run()