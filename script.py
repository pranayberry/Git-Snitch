from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def scrape(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,"lxml")
	if  soup.find_all('title') != []:
		return soup
	return None

def fname(page):
	return page.find('div','vcard-fullname').string

def contributionSummary(url):
	page = scrape(url)
	if page == None:
		print "Invalid Username"
	else:
		fullName = fname(page)
		#print "\n******************************************************"
		print "\n",fullName
		print "@%s" % username
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

def publicActivity(url):
	page = scrape(url)
	if page == None:
		print "Invalid Username"
	else:
		fullName = fname(page)
		#print "\n******************************************************"
		print "\n",fullName
		print "@%s" % username
		for elt in page.find_all('div','title'):
			print elt.get_text()

"""
def display(url):
	page = scrape(url)
	ch = 0
	if page == None:
		print "Invalid Username"
	else:
		fullName = fname(page)
		#print "\n******************************************************"
		print "\n",fullName
		print "@%s" % username
		print "\n1. Contribution Summary"
		print "2. Public Activity"
		print "Enter you choice\n> "
		ch = int(raw_input())
		if ch == 1:
			contributionSummary(page)
		else:
			publicActivity(page)
"""

username = raw_input("Enter github username\n> ")
print "\n1. Contribution Summary"
print "2. Public Activity"
ch = int(raw_input("Enter you choice\n> "))
if ch == 1:
	url = "https://github.com/" + username
	contributionSummary(url)
elif ch ==2:
	url = "https://github.com/" + username + "?tab=activity"
	publicActivity(url)
else:
	print "Invalid Choice!"