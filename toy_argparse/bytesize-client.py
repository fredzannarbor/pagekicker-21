#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:06:53 2016

@author: fred
"""

import sys

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# Configure your Bitcoin wallet.
wallet = Wallet()
requests = BitTransferRequests(wallet)

server_url = "http://0.0.0.0:5005"

def buy_fortune():

   url = server_url+'/buy?payout_address={0}'
   response = requests.get(url=url.format(wallet.get_payout_address()))
   print(response.text)

if __name__ == '__main__':

    buy_fortune()