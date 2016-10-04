#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import psutil
import subprocess
import os
import yaml

from flask import Flask
from flask import request

from two1.wallet.two1_wallet import Wallet
from two1.bitserv.flask import Payment

from revE16 import RevE16

app = Flask(__name__)
# app.debug = True

# setup wallet
wallet = Wallet()
payment = Payment(app, wallet)

# Rev helper class
rev = RevE16()

# hide logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


def get_payment_amt(request):
    """
    Return the amount of the request based on the number of days being requested.
    """
    days = request.args.get('days')
    if not days or not days.isdigit() or int(days) < 1:
        days = 1
    else:
        days = int(days)

    return days * 1000


@app.route('/')
@payment.required(get_payment_amt)
def measurement():
    """
    Queries the local device for revenue stats details.

    Returns: HTTPResponse 200 with a json containing the stats info.
    HTTP Response 400 if there is an error reading the stats.
    """
    # Get the number of days being requested
    days = request.args.get('days')
    if not days or not days.isdigit() or int(days) < 1:
        days = 1
    else:
        days = int(days)

    try:
        data = rev.getRevenue(days)
        response = json.dumps(data, indent=4, sort_keys=True)
        return response
    except ValueError as e:
        return 'HTTP Status 400: {}'.format(e.args[0]), 400


if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--daemon", default=False, is_flag=True, help="Run in daemon mode.")
    def run(daemon):
        """
        Run the service.
        """
        if daemon:
            pid_file = './revE16.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'revE16-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting revE16-server.py daemon")
        else:
            print("Server running...")
            app.run(host='0.0.0.0', port=7017)

    run()
