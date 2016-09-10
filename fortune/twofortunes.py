#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:06:53 2016

@author: fred
"""


from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests
import sys

import argparse
import ast

parser = argparse.ArgumentParser()
parser.add_argument('--data', help = "string parameters")

args = parser.parse_args()

payload = args.data
print('arg recd from cli is ' + payload)

# Configure your Bitcoin wallet.
wallet = Wallet()
requests = BitTransferRequests(wallet)

server_url = "http://0.0.0.0:5005"

def buy_fortune(key1,key2):

   url = server_url+'/buy?payout_address={0}'
   response = requests.get(url=url.format(wallet.get_payout_address()), params=payload)
   print(response.url) #debug
   print(response.text)

if __name__ == '__main__':

    payload = ast.literal_eval(payload)
    #print(payload)
    key1 = payload["key1"]
    key2 = payload["key2"]
    print(key1, ' ', key2)
    buy_fortune(key1, key2)