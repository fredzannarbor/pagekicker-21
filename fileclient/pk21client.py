#!/usr/bin/env python3
import json

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://localhost:5000/'

def buy_fortune():
       try:
       # create a 402 request with the server payout address
            url = server_url+'buy?payout_address={1}'
            answer = requests.get(url, wallet.get_payout_address()), stream=True)

            if answer.status_code != 200:
                print("Could not make an offchain payment. Please check that you have sufficient buffer.")
            else:
              

if __name__ == '__main__':
    buy_file()
