from bittrex import bittrex
import argparse
import json
import signal
import sys
import time
import os
import random
from random import randint

# Get these from https://bittrex.com/Account/ManageApiKey
def get_secret(secret_file):
    """Grabs API key and secret from file and returns them"""

    with open(secret_file) as secrets:
        secrets_json = json.load(secrets)
        secrets.close()

    return str(secrets_json['key']), str(secrets_json['secret'])
# setup api
key, secret = get_secret("secrets.json")
api = bittrex(key, secret)

# do before entering coin to save the API call during the pump
btcBalance = api.getbalance("BTC")['Available']

def sigint_handler(signum, frame):
    """Handler for ctrl+c"""
    print '\n[!] CTRL+C pressed. Exiting...'
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

print 'You have {} BTC available.'.format(btcBalance)
investmentTotal = float(raw_input("How much do you want to invest ?: "))
while investmentTotal > btcBalance:
	print 'You can\'t invest more than {}'.format(btcBalance)
	investmentTotal = float(raw_input("How much do you want to invest ?: "))

incrementSize = float(investmentTotal / 100)

btcInvested = 0.0

targetCoin = raw_input("Enter the target coin ticker name (i.e. BTC, ETH, BITB): ")

firstTargetPrice = float(raw_input("Enter the first target price: "))
secondTargetPrice = float(raw_input("Enter the second target price: "))
thirdTargetPrice = float(raw_input("Enter the third target price: "))
activeTargetPrice = firstTargetPrice

coinPrice = api.getticker("BTC-" + targetCoin)
askPrice = coinPrice['Ask']

numCoins = (incrementSize - (incrementSize)*0.00251) / askPrice

print 'Current ask price for {} is {:.8f} BTC.'.format(targetCoin, askPrice)

while btcInvested < investmentTotal:

    if incrementSize < 0.0005:
        incrementSize = 0.0005 + round(random.uniform(0, (incrementSize/1.5)), 8)
    elif incrementSize > 0.05:
        incrementSize = 0.01 + round(random.uniform(0, (incrementSize/4)), 8)
    else:
        incrementSize = incrementSize + round(random.uniform(0, (incrementSize/2)), 8))

    print "Waiting a random amount of time between 5 seconds and 25 minutes to execute buying..."
    time.sleep(randint(5,1500))
    if askPrice <= activeTargetPrice:
        print 'Current ask price for {} is {:.8f} BTC.'.format(targetCoin, askPrice)
        print "Buying {:.8f} {} at {:.8f}".format(numCoins, targetCoin, askPrice)
        print api.buylimit('BTC-' + targetCoin, numCoins, askPrice)
        btcInvested += incrementSize
        print "BTC invested so far: {:.8f} out of {:.8f}".format(btcInvested, investmentTotal)

    else:
        print "The current price of {} is {:.8f} which is greater than the active target price of {}!".format(targetCoin, askPrice, activeTargetPrice)
        toggleNextTarget = raw_input("would you like to move to the next target price? y/n: ")
        if toggleNextTarget == 'y' and activeTargetPrice == firstTargetPrice:
            activeTargetPrice = secondTargetPrice
            print "New target price set! Bot will attempt to accumulate under {}".format(activeTargetPrice)

        elif toggleNextTarget == 'y' and activeTargetPrice == secondTargetPrice:
            activeTargetPrice = thirdTargetPrice
            print "New target price set! Bot will attempt to accumulate under {}".format(activeTargetPrice)

        elif toggleNextTarget == 'y' and activeTargetPrice == thirdTargetPrice:
            print "You've reached the max accumulation target!"
            pumpItUp = raw_input("Would you like to use your remaining btc to pump it up? y/n: ")
            if pumpItUp =='y':
                incrementSize = float(investmentTotal - btcInvested)
                print api.buylimit('BTC-' + targetCoin, numCoins, askPrice)
                print "Buying {:.8f} {} at {:.8f}".format(numCoins, targetCoin, askPrice)

            else:
                print "Ok, you've chosen not to pump. The bot has accumulated what it can, and you will have to finish out the pump manually. Good luck to you, my friend!"
                break

        elif toggleNextTarget == 'n':
            print "Ok, bot will wait for the price to come back down below the active target and try to buy again."
            while askPrice > activeTargetPrice:
                print "Current Ask is {:.8f}".format(askPrice)
                print "Waiting for price to drop below active target..."
                time.sleep(60)

        else:
            toggleNextTarget = raw_input("Invalid input, please enter 'y' or 'n' without quotations: ")

print "Accumulation complete. Enjoy your profits ;)"



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
