from pinterest.client import raw_client
from pinterest.client import ApiClient

USER_SECRET = "MTQzNTgwODo0OTUxODUwNTg5MzY2Njg0NzM6MnwxMzkwNjY5MzAzOjAtLTIwMTEzMGVhMzYyYzM1NTEyZTA1NjJlNGZiYTJjMTBiN2RhMmEwZjU="
APP_SECRET = "5e0927fa47bf3e3eab3d171b4db596f9684fa75d"
APP_ID = "1435808"

'''
my_client = raw_client(APP_ID, APP_SECRET)

#response = my_client.users.icecreamcohen.pins.get()
'''

apic = ApiClient(APP_ID, APP_SECRET)
apic.authorize(USER_SECRET)





#print response