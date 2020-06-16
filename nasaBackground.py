#Built-ins
import requests
import urllib
from datetime import datetime, timedelta
import os
from appscript import app, mactypes


#NASA Open API Key
API_KEY = 'nazd4vUIi43EvaMhhQJDuaoFbMhQOBtANbIeTd7x'

def change_background_image():
	"""Changes desktop background to NASA POD pulled from API

	Arguments: None
	
	Usage: Currently only works on Macs. Ensure a valid API key is added.
	"""

	#Calculate current date and yesterday's date
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

	path = os.path.dirname(os.path.realpath(__file__))

	#Pull image url from NASA POD API
	api_response = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)
	link = api_response.json()['hdurl']
	urllib.request.urlretrieve(link, path + '/' + timestamp + '.jpg')

	#Change desktop background to NASA image and remove previous image
	app('Finder').desktop_picture.set(mactypes.File(path + '/' + timestamp + '.jpg'))

	try:
		os.remove(path + yesterday_timestamp + '.jpg')
	except:
		pass
