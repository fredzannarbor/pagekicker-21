#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import two1
from two1.commands.util import config as two1_config
from two1.server import machine_auth_wallet
from two1.server import rest_client
from two1.commands.util import wallet as wallet_utils
from datetime import datetime


class RevE16:
    """
    Revenue gathering helper class.
    """

    def __init__(self):
        """
        Constructor for the Rev class.
        """
        self.config = two1_config.Config(two1.TWO1_CONFIG_FILE, None)
        self.wallet = wallet_utils.get_or_create_wallet(self.config.wallet_path)
        self.machine_auth = machine_auth_wallet.MachineAuthWallet(self.wallet)
        self.client = rest_client.TwentyOneRestClient(two1.TWO1_HOST, self.machine_auth, self.config.username)

    def getRevenue(self, days):
        """
        Get revenue stats for the number of days being requested.
        """
        response = self.client.get_earning_logs()
        logs = response["logs"]
        logs = self._filter_rollbacks(logs)

        days_info = []
        processedDays = 0
        current_day = datetime.fromtimestamp(logs[0]["date"])
        day_rev = 0
        day_transactions = 0
        total_rev = 0
        total_transactions = 0

        # Iterate over the logs until we hit the number of days we want
        for entry in logs:
            entry_day = datetime.fromtimestamp(entry["date"])

            # Check if we have started a new day
            if current_day.date() > entry_day.date():
                processedDays = processedDays + 1

                # If we are over the number of days we care about, then bail out
                if processedDays > days:
                    break

                # Save off days data and reset vars
                total_rev = total_rev + day_rev
                total_transactions = total_transactions + day_transactions
                days_info.append({"day": current_day.strftime('%Y-%m-%d'), "revenue": day_rev, "num_transactions": day_transactions})
                day_rev = 0
                day_transactions = 0
                current_day = entry_day

            # Discard any payments we sent out
            if entry["amount"] < 0:
                continue

            # Discard any payments sent to the current user (probably just testing APIs and shouldn't really count)
            if "-" in entry["reason"]:
                buy_str = entry["reason"].split("-", 1)
                if buy_str[0] == self.config.username:
                    continue

            # Add onto the current day values
            day_transactions = day_transactions + 1
            day_rev = day_rev + entry["amount"]

        ret = {"totalRevenue": total_rev, "totalTransactions": total_transactions, "dailyStats": days_info}
        return ret

    def _filter_rollbacks(self, logs):
        # due to the payout schedule, it is guaranteed that a rollback debit is preceded by a
        # payout credit. When we see a rollback, we need to both filter that rollback and
        # its matching payout. We are bound to find the matching payout in the next iteration
        rollbacks = {}
        result = []
        for entry in logs:
            if entry["reason"] and entry["reason"] == 'PayoutRollback':
                count_for_amount = rollbacks.get(entry["amount"], 0)
                rollbacks[-entry["amount"]] = count_for_amount + 1
            elif (entry["reason"] == "flush_payout" or entry["reason"] == "earning_payout") \
                    and (entry["amount"] in rollbacks and rollbacks[entry["amount"]] > 0):
                rollbacks[entry["amount"]] -= 1
            else:
                result.append(entry)

        return result
