# Uses Google Finance module
# For formatting
# import json; print json.dumps(getQuotes(ticker)[0], indent=4)

from googlefinance import getQuotes
from time import sleep

ticker = "SGX:SK7"
while True:
    print getQuotes(ticker)[0]["LastTradePrice"]
    sleep(1)