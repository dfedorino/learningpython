import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
if len(url) < 1 : url = 'http://data.pr4e.org' # user's url
html = urllib.request.urlopen(url).read() # opens url in 'read' mode
soup = BeautifulSoup(html, 'html.parser') # ...

tags = soup('a')
for tag in tags:
    print(tags)
