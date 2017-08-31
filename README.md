# AccumuBot
A coin accumulation bot for the professionals. I spent a lot of time thinking through and implementing this bot, so if you find it useful, send a tip my way!

BTC Address: 18QXtBzaTmDj7gna7Nq1TtjgAy768KDfEB <br>
ETH Address: 0xf66a7ce86824d9b7aff9ffa86e2e6cd02c88bd23

# Getting Started & How to Use the AccumuBot

In order to get the bot up & running you'll need a coupe of things:

1. PowerShell (Windows), Terminal (OSX), or Bash (Linux) <br>
2. Python 2: https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi
3. Your own Bittrex API key & secret: https://bittrex.com/Manage#sectionApi
<br>    3a. Make sure your API key has enabled "Read Info", "Trade Limit", and "Trade Market"
<br>    3b. Make sure that "Withdraw" is DISABLED on your API

You can verify that you have Python installed correctly by typing 
```
python 
```
<br>into PowerShell and it should return the following result:

```
C:\Users\DrCoolio> python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

Next you'll need to setup the secrets.json file so that it has your API Key and Secret for the bot to reference when connecting to Bittrex. Simply copy & paste your own key and secret from bittrex into the secrets.json file in the following format:

```
{
  "key": "Paste your bittrex API key here",
  "secret": "Paste your bittrex API secret here"
}
```

Make sure you do not alter the file beyond that, and make sure the quotation marks remain there as well. Save the secrets.json file with your changes and now you're ready to start running the bot!
