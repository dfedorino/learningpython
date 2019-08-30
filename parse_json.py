import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url =  input('Enter location: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_271102.json'
#------------------------------------------------------------------------------
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx) # opens an url in the byte type
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)['comments']
sum = 0
for user in info:
   sum += int(user["count"])
print('Count: ', len(info))
print('Sum: ', sum)
