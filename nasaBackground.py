#Built-ins
import requests
import urllib
from datetime import datetime, timedelta
import os
from appscript import app, mactypes


#NASA API Key
API_KEY = '###'

def change_background_image():
	"""Changes desktop background to NASA POD pulled from API

	Arguments: None
	
	Usage: Must begin with a background image from previous day.
		   Save file in current path and run function to update image.
	"""

	now = datetime.now()
	month = str(now.month)
	day = str(now.day)
	if (now.month < 10):
		month = '0' + str(now.month)
	if (now.day < 10):
		day = '0' + str(now.day)
	year = str(now.year)
	timestamp = month + day + year

	yesterday = datetime.now() - timedelta(days = 1)
	yesterday_month = str(yesterday.month)
	yesterday_day = str(yesterday.day)
	if (yesterday.month < 10):
		yesterday_month = '0' + str(yesterday.month)
	if (yesterday.day < 10):
		yesterday_day = '0' + str(yesterday.day)
	yesterday_year = str(yesterday.year)
	yesterday_timestamp = yesterday_month + yesterday_day + yesterday_year

	path = '/Users/johnkeck/Documents/Code/Python/NASABackground/' 

	api_response = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)
	link = api_response.json()['hdurl']
	urllib.request.urlretrieve(link, path + timestamp + '.jpg')

	app('Finder').desktop_picture.set(mactypes.File(spath + timestamp + '.jpg'))

	try:
		os.remove(path + yesterday_timestamp + '.jpg')
	except:
		print("Check image files")
