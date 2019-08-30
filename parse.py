from urllib.request import urlopen # imports only one module 'urlopen' from the library urlib.request
from bs4 import BeautifulSoup # imports only one module 'BeautifulSoup' from the library bs4
import ssl # imports module to avoid certificate errors

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # a web address in a form of a string
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_271099.html' # a shortcut
html = urlopen(url, context=ctx).read() # assign a variable which contains the information about a site in the form of bytes and reads the info
soup = BeautifulSoup(html, "html.parser") # the essential part of the 'Beautiful Soup' module, represents the html page, opened with urlopen,
# as a tree of Python classes. "html.parser" here is the chosen parser for the content of the page

# Retrieve all of the anchor tags
tags = soup('span') # searches all the tags, which are mentinoed in the brackets
count = 0 # a variable to count the iterations
sumtg = 0 # a variable to count the sum of the contents
for tag in tags:
    # Look at the parts of a tag
#    print('TAG:',tag) # prints out the line with the tag
#    print('URL:',tag.get('span', None)) # as we can treat a tag like a dictionary, it's a common pattern to print out all the links on the html page
#    print('Contents:', tgcont) # prints out all the contents (including subtags) of the tag
#    print('Attrs:',tag.attrs) # prints out dictionaries where the key is the attribute of the tag and the value is the value of the attribute
    count += 1 # counts the lines with the tag
    sumtg += int(tag.contents[0]) # calculates the sum of the contents of the 'comments' tag
print("Count:", count, "\nSum:", sumtg) # prints out the result of the computations
