#!/usr/bin/env python3


from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

import argparse
import urllib

parser = argparse.ArgumentParser()
parser.add_argument('s', help = 'sentence to be translated')
args = parser.parse_args()
sentence = args.s
#print(sentence)
# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://localhost:5001/'

def buy_toy(sentence):

    sel_url = server_url+'buy?sentence='

    sentence = urllib.parse.quote_plus(sentence)
    response = requests.get(url=sel_url+sentence)
    print(response.text)

if __name__ == '__main__':
    buy_yoda(sentence)
