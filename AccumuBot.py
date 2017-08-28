from bittrex import bittrex
import argparse
import json
import signal
import sys
import time
import os
from random import randint

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

def sigint_handler(signum, frame):
    """Handler for ctrl+c"""
    print '\n[!] CTRL+C pressed. Exiting...'
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

print 'You have {} BTC available.'.format(btcBalance)
investmentTotal = float(raw_input("How do you want to invest ?: "))
while investmentTotal > btcBalance:
	print 'You can\'t invest more than {}'.format(btcBalance)
	investmentTotal = float(raw_input("How much are you going to invest ?: "))

incrementSize = float(investmentTotal / 100)

btcInvested = 0.0

firstTargetPrice = float(raw_input("Enter the first target price: "))
secondTargetPrice = float(raw_input("Enter the second target price: "))
thirdTargetPrice = float(raw_input("Enter the third target price: "))
activeTargetPrice = float(firstTargetPrice)

targetCoin = raw_input("Enter the target coin ticker name (i.e. BTC, ETH, BITB): ")

firstTargetActive  = True
secondTargetActive = False
thirdTargetActive  = False

coinPrice = api.getticker("BTC-" + targetCoin)
askPrice = coinPrice['Ask']

coinsummary = api.getmarketsummary("BTC-" + targetCoin)
clast = coinsummary[0]['Last']

print 'Current ask price for {} is {:.8f} BTC.'.format(targetCoin, askPrice)

while btcInvested < investmentTotal:
    if firstTargetActive == True:
        secondTargetActive = False
        thirdTargetActive  = False
        activeTargetPrice = float(firstTargetPrice)

    elif secondTargetActive == True:
        firstTargetActive = False
        thirdTargetActive  = False
        activeTargetPrice = float(secondTargetPrice)

    else
        thirdTargetActive == True:
        firstTargetActive = False
        secondTargetActive  = False
        activeTargetPrice = float(thirdTargetPrice)


    if askPrice < activeTargetPrice:
        time.sleep(randint(5,600))                                            # Wait a random amount of time between 5 seconds and 10 minutes to place buy order
        print api.buylimit('BTC-' + targetCoin, IDK_WHAT_GOES_HERE, askPrice) # Place a buy order of incrementSize at askPrice
        btcInvested += incrementSize                                          # Keep track of how much btc the user has invested so far compared against how much they want to invest in total
        print "BTC invested so far: {:.8f} out of {:.8f}".format(btcInvested, investmentTotal)
    else
        # Prompt user to either activate next target price to continue accumulation, or wait until askPrice is below activeTargetPrice

print "Congratulations, you are fully invested in {}. Enjoy your profits ;)".format(targetCoin)



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
