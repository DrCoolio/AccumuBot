from bittrex import bittrex
import argparse
import json
import signal
import sys
import time
import os

# Get these from https://bittrex.com/Account/ManageApiKey
def get_secret(secret_file):
    """Grabs API key and secret from file and returns them"""

    with open(secret_file) as secrets:
        secrets_json = json.load(secrets)
        secrets.close()

    return str(secrets_json['key']), str(secrets_json['secret'])
# setup api
key, secret = get_secret("secrets-b.json")
api = bittrex(key, secret)

# do before entering coin to save the API call during the pump
btcBalance = api.getbalance("BTC")['Available']

# Enables limit trading
allow_orders = True

def sigint_handler(signum, frame):
    """Handler for ctrl+c"""
    print '\n[!] CTRL+C pressed. Exiting...'
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

print 'You have {} BTC available.'.format(btcBalance)
investmentTotal = float(raw_input("How much are you going to invest ?: "))
while investmentTotal > btcBalance:
	print 'You can\'t invest more than {}'.format(btcBalance)
	investmentTotal = float(raw_input("How much are you going to invest ?: "))

incrementSize = float(investmentTotal / 100)

targetCoin = raw_input("Enter the target Coin ticker name (i.e. BTC, ETH, BITB): ")
firstTargetPrice = float(raw_input("Enter the first target price: "))
secondTargetPrice = float(raw_input("Enter the second target price: "))
thirdTargetPrice = float(raw_input("Enter the third target price: "))

coinPrice = api.getticker("BTC-" + targetCoin)
askPrice = coinPrice['Ask']

coinsummary = api.getmarketsummary("BTC-" + targetCoin)
clast = coinsummary[0]['Last']

print 'Current ask price for {} is {:.8f} BTC.'.format(targetCoin, askPrice)










def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
