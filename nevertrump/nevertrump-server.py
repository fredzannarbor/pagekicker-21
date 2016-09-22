#!/usr/bin/env python3

import subprocess
from flask import Flask
import os
import psutil

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# machine-payable endpoint that returns fortune if payment made
@app.route('/buy')
@payment.required(2750)
def buy_fortune():

    fortune = subprocess.check_output(['fortune', 'nevertrump'])
    return fortune

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")
    def run(daemon):
        if daemon:
            pid_file = './nevertrump.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'nevertrump-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting nevertrump-server.py daemon")
        else:
            print("nevertrump server running...")
            app.run(host='::', port=5004)

    run()