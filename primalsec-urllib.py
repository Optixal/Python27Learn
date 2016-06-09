import urllib
from bs4 import BeautifulSoup
import statuscc

RHOST = 'http://127.0.0.1'
request = urllib.urlopen(RHOST)

print request.getcode()
print request.headers  # ['server']

parsed = BeautifulSoup(request.read(), "lxml")

print parsed.title
print parsed.h1
paragraphs = parsed.find_all('p')
print paragraphs


