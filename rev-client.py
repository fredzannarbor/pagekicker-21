#!/usr/bin/python3
import logging
import json

from two1.commands.util import config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests
requests = BitTransferRequests(Wallet(), config.Config().username)

logger = logging.getLogger(__name__)


def gatherRevenue(host, website, days):
    """
    Retrieves 30 days of revenue stats from host and uploads to website.
    """
    # Get the rev stats from the host
    clientUrl = "http://" + host + ":7017?days={}".format(days)
    ret = requests.get(clientUrl).text
    logger.debug(ret)
    data = json.loads(ret)

    # Upload it to the site
    postHeaders = {"client": "asdfasdf"}
    ret = requests.post(website + "/stat/revenue", json=data, headers=postHeaders)

    # Print results
    if ret.json()['success'] is True:
        logger.info("Successfully saved revenue stats")
    else:
        logger.warn("Failed to upload revenue stats: {}".format(ret.text))

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-h", "--host", default="localhost", help="21 Node running RevE16 to gather stats from.")
    @click.option("-w", "--website", default="http://www.esixteen.co", help="Website to upload results to.")
    @click.option("-d", "--days", default=1, help="Number of days to gather stats for.")
    @click.option("-l", "--log", default="INFO", help="Logging level to use (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    def run(host, website, days, log):
        """
        Run the app.
        """
        print("in main")
        # Set logging level
        numeric_level = getattr(logging, log.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % log)
        logging.basicConfig(level=numeric_level)

        # Run
        logger.info("Running revenue gathering for {} days against node: {} and uploading results to: {}".format(days, host, website))
        gatherRevenue(host, website, days)

    run()
