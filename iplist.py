import urllib
from bs4 import BeautifulSoup
import coloredstatus as cs

ip = raw_input(cs.status + "Enter ip address to inspect: ")
print cs.status + "Finding websites associated with " + ip + "..."
request = urllib.urlopen('http://iplist.net/' + ip)
parsed = BeautifulSoup(request.read(), "lxml")

associated_websites = parsed.find_all('h2')
for website in associated_websites:
    print cs.good + str(website)[4:-5]
