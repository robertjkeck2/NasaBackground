from appscript import app, mactypes
import requests
import urllib
from datetime import datetime, timedelta
import os

API_KEY = 'nazd4vUIi43EvaMhhQJDuaoFbMhQOBtANbIeTd7x'

class nasaBackground():

	def __init__(self):

		now = datetime.now()
		month = str(now.month)
		day = str(now.day)
		if (now.month < 10):
			month = '0' + str(now.month)
		if (now.day < 10):
			day = '0' + str(now.day)
		year = str(now.year)
		self.timestamp = month + day + year

		yesterday = datetime.now() - timedelta(days = 1)
		yesterday_month = str(yesterday.month)
		yesterday_day = str(yesterday.day)
		if (yesterday.month < 10):
			yesterday_month = '0' + str(yesterday.month)
		if (yesterday.day < 10):
			yesterday_day = '0' + str(yesterday.day)
		yesterday_year = str(yesterday.year)
		self.yesterday_timestamp = yesterday_month + yesterday_day + yesterday_year

		self.path = '/Users/johnkeck/Documents/Code/Python/NASABackground/' 

	def change_background_image(self):

		api_response = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)
		link = api_response.json()['hdurl']
		urllib.request.urlretrieve(link, self.path + self.timestamp + '.jpg')

		app('Finder').desktop_picture.set(mactypes.File(self.path + self.timestamp + '.jpg'))

		try:
			os.remove(self.path + self.yesterday_timestamp + '.jpg')
		except:
			print("Check image files")
