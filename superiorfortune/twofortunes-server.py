# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:44:35 2016

@author: fred
"""
import subprocess
import os
import psutil
from flask import Flask
from flask import request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/fortune', methods=['GET', 'POST'])
@payment.required(3000)
def buy_fortune():

    key1 = str(request.args.get('key1'))
    key2 = str(request.args.get('key2'))
    print('keys are' + ' ' + key1 + ' ' +key2)
    fortune = subprocess.check_output(['fortune', key1, key2])
    return fortune

# Initialize and run the server
if __name__ == '__main__':

   import click

   @click.command()
   @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")

   def run(daemon):
            if daemon:
                pid_file = './twofortunes.pid'
                if os.path.isfile(pid_file):
                    pid = int(open(pid_file).read())
                    os.remove(pid_file)
                    try:
                        p = psutil.Process(pid)
                        p.terminate()
                    except:
                        pass
                try:
                    p = subprocess.Popen(['python3', 'twofortunes-server.py'])
                    open(pid_file, 'w').write(str(p.pid))
                except subprocess.CalledProcessError:
                    raise ValueError("error starting twofortunesserver.py daemon")
            else:
                print("twofortunes-server running...")
                app.run(host='::', port=5006)
   run()