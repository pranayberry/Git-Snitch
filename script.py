from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def scrape(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,"lxml")
	if  soup.find_all('p') == []:
		return soup
	return None

def display(url):
	page = scrape(url)
	if page == None:
		print "Invalid Username"
	else:
		print "scrape successful"



username = raw_input("Enter github username\n> ")
url = "https://github.com/" + username
display(url)
