#!/usr/bin/env python3

import os
import subprocess
import json
import yaml
from flask import Flask


from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# machine-payable endpoint that returns fortune if payment made
@app.route('/buy')
@payment.required(1000)
def buy_fortune():

    fortune = subprocess.check_output(['fortune', 'wizardfacts'])
    return fortune

@app.route('/manifest')
def docs():
    '''
    Serves the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")
    def run(daemon):
        if daemon:
            pid_file = './wizardfacts.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'wizardfacts-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting wizardfacts-server.py daemon")
        else:
            print("Wizardfacts server running...")
            app.run(host='0.0.0.0', port=5003)

    run()