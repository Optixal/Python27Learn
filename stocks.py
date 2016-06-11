# Grabs from <span> tag on Google Finance page

import urllib
from bs4 import BeautifulSoup
from time import sleep

ticker = "SGX:SK7"
url = "https://www.google.com/finance?q=" + ticker

while True:
    request = urllib.urlopen(url)
    parsed = BeautifulSoup(request.read(), "lxml")
    print parsed.findAll('span', {'class': 'pr'})[0].text.strip()
    # print parsed.find('span', id='ref_' + str(stockid) + '_l').text # for id
    sleep(1)