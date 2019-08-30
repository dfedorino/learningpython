import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url =  input('Enter location: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_271101.xml'
#------------------------------------------------------------------------------
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx) # opens an url in the byte type
data = uh.read()
print('Retrieved', len(data), 'characters')
#------------------------------------------------------------------------------
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
lst1 = list()
sum = 0
for item in lst:
    cnt = int(item.find('count').text)
    lst1.append(cnt)
    sum += cnt
print('Sum: ', sum)
print('Count: ', len(lst1))
