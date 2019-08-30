import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

lnk = 'http://py4e-data.dr-chuck.net/known_by_Amilie.html'# input('Enter URL: ')
place = 18 # int(input("Enter the position:"))
links_to_follow = 7 # int(input("Enter counts:"))
def getlink(url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    links = list()
    for tag in tags:
        links.append(tag.get('href', None))
    return (links[place - 1])

result = getlink(lnk)

for i in range(1, (links_to_follow)):
    result = getlink(result)
    print("Retrieving: ", result)
