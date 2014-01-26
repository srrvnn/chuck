from pinterest.client import raw_client
from pinterest.client import ApiClient
from pymongo import MongoClient
import urllib2
import json

APP_SECRET = "5e0927fa47bf3e3eab3d171b4db596f9684fa75d"
APP_ID = "1435808"

def getUserRetailPins(USER_SECRET,user_id):
    userpins = getUserPins(USER_SECRET,user_id)
    client = MongoClient('107.170.247.246', 27017)
    records = client['chuck']['retailers'].find()
    retail_pins = {}
    for record in records:
	items = record['items']
	for item in items:
	    retail_pins[item['pinid']] = 1
    ret = []
    print retail_pins
    for pin in userpins:
	if 'origin_pin' in pin.keys() and pin['origin_pin']!=None and 'id' in pin['origin_pin'].keys() and pin['origin_pin']['id'] in retail_pins.keys():
	    #print 'in: '+pin['origin_pin']['id']
	    origin_pin_data = getPinDetails(pin['origin_pin']['id'])
	    origin_pinner_data = getUserDetails(origin_pin_data['pinner']['id']) 
	    pin['origin_pin']['full_name'] = origin_pinner_data['full_name']
	    pin['origin_pin']['image_small_url'] = origin_pinner_data['image_small_url']
	    pin['origin_pin']['profile_link'] = 'http://pinterest.com/'+origin_pinner_data['username']
	    ret.append(pin)
    return ret

def getUserDetails(user_id):
    user_url = 'https://api.pinterest.com/v3/users/'+user_id+'/?access_token=MTQzMTU5NDo0Njk5OTMwNDg1MjEwNjgwOTA6MnwxMzkwNjg1ODI5OjAtLTRhYTc0NzA4YjU3YmEyNDM1ODBkMmNiZTZiNWNkNGM4YTJhYzgzM2U='
    response = urllib2.urlopen(user_url).read()
    response = json.loads(response)
    if 'data' in response.keys():
	return response['data']
    else:
	return None
  
  
def getPinDetails(pin_id):
    #other params unsupported now
    pin_url = 'https://api.pinterest.com/v3/pins/'+pin_id+'/?access_token=MTQzMTU5NDo0Njk5OTMwNDg1MjEwNjgwOTA6MnwxMzkwNjg1ODI5OjAtLTRhYTc0NzA4YjU3YmEyNDM1ODBkMmNiZTZiNWNkNGM4YTJhYzgzM2U='
    response = urllib2.urlopen(pin_url).read()
    response = json.loads(response)
    if 'data' in response.keys():
	return response['data']
    else:
	return None
  
def getUserPins(USER_SECRET,user_id):
    my_client = raw_client(APP_ID, APP_SECRET)
    my_client.authorize(USER_SECRET)
    pins = my_client.users(user_id).pins.get()
    return pins[0]

