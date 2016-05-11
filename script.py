from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def scrape(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,"lxml")
	if  soup.find_all('p') == []:
		return soup
	return None

def fname(page):
	return page.find('div','vcard-fullname').string

def contribution(page):
	i = 0
	print "\nContribution Summary\n"
	print "Date\t\t\tNo of Contributions"
	while i<5:
		for day in page.find_all('rect'):
			properties = day.attrs
			date = datetime.today() - timedelta(i)
			date = date.strftime("%Y-%m-%d")
			if properties['data-date'] == date:
				print date,"\t\t\t",
				print properties['data-count']
		i += 1


def display(url):
	page = scrape(url)
	if page == None:
		print "Invalid Username"
	else:
		fullName = fname(page)
		#print "\n******************************************************"
		print "\n",fullName
		print "@%s" % username
		contribution(page)


username = raw_input("Enter github username\n> ")
url = "https://github.com/" + username
display(url)
