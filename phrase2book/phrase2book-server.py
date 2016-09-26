# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:44:35 2016

@author: fred
"""
import subprocess
import os
import psutil
from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/bookbuild', methods=['GET', 'POST'])
@payment.required(10000)
def book_build():

    singleseed = str(request.args.get('singleseed'))
    print('singleseed is' + singleseed)
    book_build = subprocess.check_output(['/home/fred/pagekicker-community/scripts/bin/create-catalog-entry.sh', '--singleseed', singleseed])
    return book_build

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
                    p = subprocess.Popen(['python3', 'phrase2book-server.py'])
                    open(pid_file, 'w').write(str(p.pid))
                except subprocess.CalledProcessError:
                    raise ValueError("error starting phrase2book daemon")
            else:
                print("phrase2book-server running...")
                app.run(host='::', port=5008, debug=True)
   run()