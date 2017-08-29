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
activeTargetPrice = firstTargetPrice

targetCoin = raw_input("Enter the target coin ticker name (i.e. BTC, ETH, BITB): ")

firstTargetActive  = True
secondTargetActive = False
thirdTargetActive  = False

coinPrice = api.getticker("BTC-" + targetCoin)
askPrice = coinPrice['Ask']

numCoins = (incrementSize - (incrementSize)*0.00251)) / askPrice

while btcInvested < investmentTotal:
    print 'Current ask price for {} is {:.8f} BTC.'.format(targetCoin, askPrice)
    if askPrice <= activeTargetPrice:
        time.sleep(randint(5,600))
        print "Buying {:.8f} {} at {:.8f}".format(numCoins, targetCoin, askPrice)
        print api.buylimit('BTC-' + targetCoin, numCoins, askPrice)
        btcInvested += incrementSize
        print "BTC invested so far: {:.8f} out of {:.8f}".format(btcInvested, investmentTotal)

    else:
        print "The current price of {} is {:.f} which is greater than the active target price!".format(targetCoin, askPrice)
        toggleNextTarget = raw_input("would you like to move to the next target price? y/n: ")
            if toggleNextTarget == 'y' and firstTargetActive == True:
                firstTargetActive = False
                secondTargetActive = True
                activeTargetPrice = secondTargetPrice

            elif toggleNextTarget == 'y' and secondTargetActive == True:
                secondTargetActive = False
                thirdTargetActive == True
                activeTargetPrice = thirdTargetPrice

            elif toggleNextTarget == 'y' and thirdTargetActive == True:
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
                print "Ok, I will wait for the price to come back down below the active target and try to buy again."

            else:
                toggleNextTarget raw_input("Invalid input, please enter 'y' or 'n' without quotations: ")

else:
    break

print "Accumulation complete. Enjoy your profits ;)"



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
