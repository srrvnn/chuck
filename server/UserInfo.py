from pinterest.client import raw_client
from pinterest.client import ApiClient


APP_SECRET = "5e0927fa47bf3e3eab3d171b4db596f9684fa75d"
APP_ID = "1435808"

def getUserRetailPins(USER_SECRET,user_id):
  my_client = raw_client(APP_ID, APP_SECRET)
  my_client.authorize(USER_SECRET)
  pins = my_client.users(user_id).pins.get()
  retail_pins = []
  for pin in pins:
    retail_pins.append(pin)
  return retail_pins
