# AccumuBot
A coin accumulation bot for the professionals. I spent a lot of time thinking through and implementing this bot, so if you find it useful, send a tip my way!

BTC Address: 18QXtBzaTmDj7gna7Nq1TtjgAy768KDfEB <br>
ETH Address: 0xf66a7ce86824d9b7aff9ffa86e2e6cd02c88bd23

# Getting Started

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
into PowerShell (or whichever you use) and it should return the following result:

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

# Running AccumuBot

In order to start using AccumuBot, begin by navigating to the folder containing the AccumuBot.py file (this folder should also have your secrets.json and bittrex.py files). In the examples my folder is located on my Desktop

```
C:\Users\DrCoolio> cd Desktop\AccumuBot
```
Once you have navigated to the appropriate folder, run the bot:
```
C:\Users\DrCoolio\Desktop\AccumuBot> python AccumuBot.py
```
The bot will print the total available BTC in your bittrex account, it will then ask you how much BTC you would like to invest in your accumulation. 
```
You have 10.572 BTC available.
How much do you want to invest ?: 0.5
```
Then the bot will ask you what coin you wish to accumulate:
```
Enter the target coin ticker name (i.e. BTC, ETH, BITB): XVG
```
After you've told the bot the coin it will ask you three target prices. At any given time the bot will NOT place buy-orders if the Ask price is above the "active" target price. The first target price defaults to active, and the second and third are activated sequentially later in the bot's progression.
```
Enter the first target price: 0.00000125
Enter the second target price: 0.00000200
Enter the third target price: 0.00000250
```
The bot will then begin to accumulate the coin. It will randomly wait anywhere between 5 seconds and 1,296 seconds (21.6 minutes) between each buy-in order (so as to make the accumulation more subtle and undetected). Each buy-in will constitute 1% of the total amount you told the bot to use to invest, or a minimum of 50,000satoshi as you cannot place buy orders for less than that on Bittrex.
<br>If the Ask price goes above the target price you will be prompted to activate the next target price:
```
would you like to move to the next target price? y/n: y
```
If you enter 'y' then the next target price will become active the bot will resume buying until the Ask price has gone above the new active target, at which point you will be prompted again to change the target price. 

<br>If you enter 'n' then the bot will continuously check the Ask price of the coin every 30 seconds and will not resume buying until the Ask price has dipped back under the active target price.

<br>Once there are no more targets to reach for and you enter 'y' the bot will tell you that you've reached the final accumulation target and prompt you to "pump it up":
```
You've reached the max accumulation target!
Would you like to use your remaining btc to pump it up? y/n: y
```
If you enter 'y' then the bot will subtract the amount of BTC you have already invested from the total amount you told the bot to invest with and buy-in with the remainder at Ask price.

<br>If you enter 'n' here, then the bot will terminate and you will be on your own for pumping or further accumulation if you wish. 

<br>Finally if you chose not to pump, or if the bot has gone through all of it's accumulations successfuly and used up all of the volume of BTC you told it you wanted to invest with it will exit and you'll be on your own to sell your coins at whatever profit you like.

```
Accumulation complete. Enjoy your profits ;)
```

I hope this bot works out for yoU! I spent a lot of time thinking through and implementing this code, so if you find it useful, send a tip my way!

BTC Address: 18QXtBzaTmDj7gna7Nq1TtjgAy768KDfEB <br>
ETH Address: 0xf66a7ce86824d9b7aff9ffa86e2e6cd02c88bd23
