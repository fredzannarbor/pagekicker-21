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




def buy_toy():


    toy = subprocess.check_output(['fortune', 'flag1', 'flag2'])
    return toy

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
            pid_file = './toy.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'toy_argparse-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting toy_argparse-server.py daemon")
        else:
            print("toy_argparse server running...")
            app.run(host='0.0.0.0', port=5005)

    run()
