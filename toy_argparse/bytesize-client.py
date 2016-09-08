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

server_url = "http://127.0.0.1:5005"

def send_fortunefiles(fortunefile1):
    fortune_url = server_url + '/fortune?fortunefile1={0}'
    fortune = requests.get(url=fortune_url.format(fortunefile1))
    return fortune

if __name__ == '__main__':
    fortunefile1 = sys.argv[1]
    fortunefile2 = sys.argv[2]
    send_fortunefiles(fortunefile1)