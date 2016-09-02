# RevE16

## Overview
RevE16 is a bitcoin payable web app designed for the 21 Marketplace that allows users to sell statistics about the revenue that their
node is generating.  The goal is to understand what services are actually generating revenue and to help other nodes determine
if it is worth it to run specific services.

## Fees
By default, the service will charge 1000 satoshis for every day of revenue stats you ask for.

## How to Use
If you want to get stats from a node running this service, it is as simple as:
```
$ 21 buy http://localhost:7017?days=3
```
This returns 3 days worth of stats:
```
{
    "dailyStats": [
        {
            "day": "2016-09-02",
            "num_transactions": 3,
            "revenue": 9000
        },
        {
            "day": "2016-09-01",
            "num_transactions": 1,
            "revenue": 3000
        },
        {
            "day": "2016-08-31",
            "num_transactions": 1,
            "revenue": 3000
        }
    ],
    "totalRevenue": 15000,
    "totalTransactions": 5
}
```
## How to Run
If you want to run this on your node, just clone the project to your system and run as a daemon:
```
$ git clone https://github.com/pooleja/RevE16.git
$ cd RevE16
$ python3 revE16-server.py -d
```

## Make Sure it Stays Running
To ensure the server stays running across reboots, you can create a reboot cron job.  This will ensure the RevE16 will be restarted any time the device comes back online.

To open the cron file:
```
$ crontab -e
```

Edit the file and add a reboot line (replace the path):
```
@reboot cd /your/path/to/RevE16/ && python3 revE16-server.py -d
```

Now you can reboot the device and ensure it is running:
```
$ ps aux | grep python3
twenty     545  2.2  2.5  39928 25884 ?        Sl   17:35   0:07 python3 revE16-server.py
```
