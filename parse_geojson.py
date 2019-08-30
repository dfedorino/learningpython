import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False # ???
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False: # the conditional statement to use Dr. Chuck's API
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True: # the infinite loop to let the user iput as many addresses as he wants
    address = input('Enter location: ') # here we get a name of the desired location
    if len(address) < 1: break # conditional statement to break the loop to end up the program

    parms = dict() # an empty dictionary
    parms['address'] = address # parms = {'address': location}
    if api_key is not False: parms['key'] = api_key # conditional statement to use a different API key from Google Maps
    url = serviceurl + urllib.parse.urlencode(parms) # concatenating the url of the .json document and the encoded data from the parms dictionary
# the output of the concatenating is http://py4e-data.dr-chuck.net/json?address=JADAVPUR+UNIVERSITY&key=42

    print('Retrieving', url) # a message to check the address of the JSON file
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
#-------------------------------------------------------------------------------
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    json.dumps(js, indent=4)
#-------------------------------------------------------------------------------
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    # print(location)
    id = js['results'][0]['place_id']
    print('Place id: ', id)
