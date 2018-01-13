# AccumuBot

# Getting Started

In order to get the bot up & running you'll need a few things:

1. Python 2: https://www.python.org
2. PyCharm IDE: https://www.jetbrains.com/pycharm/download/#section=windows
3. Your own Bittrex API key & secret: https://bittrex.com/Manage#sectionApi
<br>    3a. Make sure your API key has enabled "Read Info", "Trade Limit", and "Trade Market"
<br>    3b. Make sure that "Withdraw" is DISABLED on your API

First, you'll need to setup the secrets.json file so that it has your API Key and Secret for the bot to reference when connecting to Bittrex. Simply copy & paste your own key and secret from bittrex into the secrets.json file in the following format:

```
{
  "key": "Paste your bittrex API key here",
  "secret": "Paste your bittrex API secret here"
}
```

Make sure you do not alter the file beyond that, and make sure the quotation marks remain there as well. Save the secrets.json file with your changes and now you're ready to start running the bot!

# Running AccumuBot

In order to use AccumuBot, simply make sure you have Python 2 installed, as well as PyCharm. Open the AccumuBot.py file with PyCharm and press the "run" button.

Once the bot is running the GUI will render and you can set the total amount of Bitcoin you wish to invest, choose the target you want to accumulate, and the price ceiling you want to accumulate under. You can then press "Start AccumuBot" and let the program do the rest.

If at any point you wish you change the price ceiling, simply enter a new value-in in the related box and press the "set new buy-in ceiling" button.

I hope this bot works out for yoU! I spent a lot of time thinking through and implementing this code, so if you find it useful, send a tip my way!

BTC Address: 18QXtBzaTmDj7gna7Nq1TtjgAy768KDfEB <br>
ETH Address: 0xf66a7ce86824d9b7aff9ffa86e2e6cd02c88bd23
