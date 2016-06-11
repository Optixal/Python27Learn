import urllib
import sys
import coloredstatus as cs
from bs4 import BeautifulSoup
from googlefinance import getQuotes
from time import sleep
from decimal import Decimal


ticker = "SGX:SK7"
refresh = 1
closecheck = 300

print cs.status + "Tracking price of " + ticker
url = "https://www.google.com/finance?q=" + ticker
closecount = 0
oldprice = 0
while True:
    price = getQuotes(ticker)[0]["LastTradePrice"]
    if Decimal(price) > Decimal(oldprice):
        print cs.good + price
    elif Decimal(price) < Decimal(oldprice):
        print cs.error + price
    oldprice = price

    # Checks if market has closed every closecheck amount
    if closecount % closecheck == 0:
        request = urllib.urlopen(url)
        parsed = BeautifulSoup(request.read(), "lxml")
        try:
            closetext = parsed.findAll('span', {'class': 'nwp'})[0].text.strip()
            if "Close" in closetext:
                print cs.warning + "Market has closed."
                sys.exit(0)
        except: pass
    closecount += 1

    sleep(refresh)