from Tkinter import *
from bittrex import bittrex
import json
import random
from random import randint


# ********** Handle Bittrex API Key & Secret **********

def get_secret(secret_file):
    """Grabs API key and secret from file and returns them"""

    with open(secret_file) as secrets:
        secrets_json = json.load(secrets)
        secrets.close()

    return str(secrets_json['key']), str(secrets_json['secret'])


key, secret = get_secret("secrets.json")
api = bittrex(key, secret)


# ********** Variable Initializations **********

activeTargetPrice = 0.0
btcInvested = 0.0
buyIn = True

# ********** Function Definitions **********

def setPriceCeiling():

    global activeTargetPrice

    activeTargetPrice = priceCeiling_Entry.get()
    activeTargetPrice = float(activeTargetPrice)
    activeTargetPrice = round(activeTargetPrice, 8)

    status_Label['text'] = "STATUS: New Price Ceiling Set at {:.8f} BTC".format(activeTargetPrice)


def stopAccumuBot():

    global buyIn

    buyIn = False
    status_Label['text'] = "STATUS: Bot stopped. Press 'Resume AccumuBot' to continue."
    runAccumubot_Button['text'] = "Resume AccumuBot"


def runAccumuBot():

    global activeTargetPrice
    global buyIn

    buyIn = True

    runAccumubot_Button['text'] = "Start AccumuBot"

    activeTargetPrice = priceCeiling_Entry.get()
    activeTargetPrice = float(activeTargetPrice)
    activeTargetPrice = round(activeTargetPrice, 8)

    investmentTotal = investmentTotal_Entry.get()
    investmentTotal = float(investmentTotal)
    investmentTotal = round(investmentTotal, 8)

    incrementSize = float(investmentTotal / 100)
    incrementSize = round(incrementSize, 8)

    targetCoin = targetCoin_Entry.get()

    coinPrice = api.getticker("BTC-" + targetCoin)
    askPrice = coinPrice['Ask']

    numCoins = (incrementSize - (incrementSize * 0.00251)) / askPrice

    def accumulate():

        def buyOrWait():

            global btcInvested

            if buyIn:
                if askPrice <= activeTargetPrice:
                    btcInvested += incrementSize
                    status_Label['text'] = "STATUS: Bought {:.8f} {} at {:.8f}...BTC invested so far: {:.8f} out of {:.8f}".format(numCoins, targetCoin, askPrice, btcInvested, investmentTotal)
                    root.after(15000, accumulate)

                else:
                    status_Label['text'] = "STATUS: Current Ask Price is {:.8f}. Waiting for price to drop below active target...BTC invested so far: {:.8f} out of {:.8f}".format(askPrice, btcInvested, investmentTotal)
                    root.after(randint(1000, 60000), buyOrWait)
            else:
                status_Label['text'] = "STATUS: Bot stopped. Press 'Resume AccumuBot' to continue."

        if buyIn:
            if btcInvested < investmentTotal:
                incrementSize = float(investmentTotal / 100)
                if incrementSize < 0.0005:
                    incrementSize = 0.0005 + round(random.uniform(0, (incrementSize*2)), 8)
                elif incrementSize > 0.05:
                    incrementSize = 0.01 + round(random.uniform(0, (incrementSize/2)), 8)
                else:
                    incrementSize = incrementSize + round(random.uniform(0, (incrementSize)), 8)

                status_Label['text'] = "STATUS: Currently waiting a random amount of time between 5 seconds and 25 minutes to execute buying...BTC invested so far: {:.8f} out of {:.8f}".format(btcInvested, investmentTotal)
                root.after(randint(5000, 1500000), buyOrWait)
            else:
                status_Label['text'] = "STATUS: {:.8f} out of {:.8f} BTC Invested! Accumulation Complete! Enjoy your profits! ;)".format(btcInvested, investmentTotal)

        else:
            status_Label['text'] = "STATUS: Bot stopped. Press 'Resume AccumuBot' to continue."

    accumulate()


root = Tk()
root.title("AccumuBot DEMO MODE")


# ********** Core Settings Section **********

# *** Total BTC to Invest ||| Label(), Entry(), and Button() ***

investmentTotal_Label = Label(root, text="How much $BTC do you want to invest: ")
investmentTotal_Entry = Entry(root)

investmentTotal_Label.grid(sticky=E)
investmentTotal_Entry.grid(row=0, column=1, pady=10, sticky=W)


# *** Target Coin ||| Label(), Entry(), and Button() ***

targetCoin_Label = Label(root, text="Enter the target coin ticker name (i.e. BTC, ETH, BITB): ")
targetCoin_Entry = Entry(root)

targetCoin_Label.grid(row=1, sticky=E)
targetCoin_Entry.grid(row=1, column=1, pady=10, sticky=W)


# *** Active Buy-in Ceiling ||| Label(), Entry(), and Button() ***

priceCeiling_Label = Label(root, text="Enter a buy-in ceiling: ")
priceCeiling_Entry = Entry(root)
priceCeiling_Button = Button(root, text="Set New Buy-in Ceiling", command=setPriceCeiling)

priceCeiling_Label.grid(row=2, column=0, sticky=E, pady=10)
priceCeiling_Entry.grid(row=2, column=1, sticky=W)
priceCeiling_Button.grid(row=2, column=2, sticky=W)


# ********** Start & Stop Buttons Section **********

# *** Start the Bot ||| Button() ***

runAccumubot_Button = Button(root, text="Start AccumuBot", command=runAccumuBot)

runAccumubot_Button.grid(row=4, column=0, pady=10)

# *** Stop the Bot ||| Button() ***

stopAccumubot_button = Button(root, text="Stop AccumutBot", command=stopAccumuBot)

stopAccumubot_button.grid(row=4, column=1)


# ********** Status & Alerts Log Section **********

# *** Status & Alerts ||| Label() ***

status_Label = Label(root, text="Welcome to AccumuBot!", relief=RIDGE)
status_Label.grid(rowspan=6, padx=25, pady=15, columnspan=10)

root.geometry("600x250")
root.mainloop()
