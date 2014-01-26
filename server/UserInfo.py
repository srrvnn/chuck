from pinterest.client import raw_client
from pinterest.client import ApiClient
from pymongo import MongoClient

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
    for pin in userpins:
	if 'origin_pin' in pin.keys() and pin['origin_pin']['id'] in retail_pins.keys():
	    ret.append(pin)
    return ret
  
def getUserPins(USER_SECRET,user_id):
    my_client = raw_client(APP_ID, APP_SECRET)
    my_client.authorize(USER_SECRET)
    pins = my_client.users(user_id).pins.get()
    return pins[0]

