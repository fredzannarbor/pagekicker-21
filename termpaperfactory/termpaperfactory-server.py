# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:44:35 2016

@author: fred
"""
import subprocess
import os
import psutil
from flask import Flask, request, send_from_directory, send_file
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
commandpath = config.get("Paths", "commandpath")
mycwd = config.get("Paths", "mycwd")
print('local commandpath and working directory are ' + commandpath, mycwd)


from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/buildtermpaper', methods=['GET', 'POST'])
@payment.required(10000)
def buy_buildtermpaper():

    key1 = str(request.args.get('key1'))
    command =  [ commandpath, key1]
    status = subprocess.check_call(command, cwd = mycwd)
    status = ('exiting with status ' + str(status))
    # print(status)
    return send_from_directory('/tmp/pagekicker/', 'delivery.docx')


# Initialize and run the server
if __name__ == '__main__':

   import click

   @click.command()
   @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")

   def run(daemon):
            if daemon:
                pid_file = './termpaperfactory.pid'
                if os.path.isfile(pid_file):
                    pid = int(open(pid_file).read())
                    os.remove(pid_file)
                    try:
                        p = psutil.Process(pid)
                        p.terminate()
                    except:
                        pass
                try:
                    p = subprocess.Popen(['python3', 'termpaperfactory-server.py'])
                    open(pid_file, 'w').write(str(p.pid))
                except subprocess.CalledProcessError:
                    raise ValueError("error starting termpaperfactory-server.py daemon")
            else:
                print("termpaperfactory running on port 5010...")
                app.run(host='::', port=5010, debug=True)
   run()
