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
investmentTotal = float(raw_input("How much do you want to invest ?: "))
while investmentTotal > btcBalance:
	print 'You can\'t invest more than {}'.format(btcBalance)
	investmentTotal = float(raw_input("How much do you want to invest ?: "))

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

numCoins = (incrementSize - (incrementSize)*0.00251)) / askPrice

print 'Current ask price for {} is {:.8f} BTC.'.format(targetCoin, askPrice)

while btcInvested < investmentTotal:
    if askPrice < activeTargetPrice:
        time.sleep(randint(5,600))                                            # Wait a random amount of time between 5 seconds and 10 minutes to place buy order
        print api.buylimit('BTC-' + targetCoin, numCoins, askPrice)           # Place a buy order of incrementSize at askPrice
        btcInvested += incrementSize                                          # Keep track of how much btc the user has invested so far compared against how much they want to invest in total
        print "BTC invested so far: {:.8f} out of {:.8f}".format(btcInvested, investmentTotal)

    else
        print "The current price of {} is {:.f} which is above the active target price!".format(targetCoin, askPrice)
        toggleNextTarget = raw_input("would you like to move to the next target price? y/n: ")
            if toggleNextTarget == 'y' or toggleNextTarget == 'yes' and firstTargetActive == True and secondTargetActive == False and thirdTargetActive == False:
                firstTargetActive = False
                secondTargetActive = True
                activeTargetPrice = float(secondTargetPrice)

            elif toggleNextTarget == 'y' or toggleNextTarget == 'yes'  and firstTargetActive == False and secondTargetActive == True and thirdTargetActive == False:
                secondTargetActive = False
                thirdTargetActive == True
                activeTargetPrice = float(thirdTargetPrice)

            elif toggleNextTarget == 'y' or toggleNextTarget == 'yes'  and firstTargetActive == False and secondTargetActive == False and thirdTargetActive == True:
                print "You've reached the max accumulation target!"
                # Prompt user to buy-in with whatever uninvested BTC they have left at this point(investmentTotal - btcInvested)

print "Congratulations, you have filled your investment in {}. Enjoy your profits ;)".format(targetCoin)



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
