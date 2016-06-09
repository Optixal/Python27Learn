import urllib
from bs4 import BeautifulSoup
import statuscc

ip = raw_input(statuscc.NEUTRAL + "Enter ip address to inspect: ")
print statuscc.NEUTRAL + "Finding websites associated with " + ip + "..."
request = urllib.urlopen('http://iplist.net/' + ip)
parsed = BeautifulSoup(request.read(), "lxml")

associated_websites = parsed.find_all('h2')
for website in associated_websites:
    print statuscc.POSITIVE + str(website)[4:-5]
