import urllib
from bs4 import BeautifulSoup

RHOST = 'http://127.0.0.1'
request = urllib.urlopen(RHOST)

print request.getcode()
print request.headers  # ['server']

parsed = BeautifulSoup(request.read(), "lxml")

print parsed
print parsed.title
print parsed.h1
paragraphs = parsed.find_all('p')   # Find multiple html tags
# Find classes  # print parsed.findAll('span', {'class': 'pr'}).text.strip()
# Find id       # print parsed.find('span', id='pr').text
print paragraphs


