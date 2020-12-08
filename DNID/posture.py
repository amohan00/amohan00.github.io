#Python program to scrape website  
#and save data from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

def pitt_posture():
	# Download HTML from website
	URL = "https://www.coronavirus.pitt.edu/"
	page = requests.get(URL) 

	# Soup Objects to find data 
	soup = BeautifulSoup(page.content, 'html.parser')
	section = soup.find(class_="views-field views-field-views-conditional")
	group = section.find_all('div', class_='')
	postures = []
	#f = open("posture.txt", "w")
	for x in group:
		# Print risk posture
		stat = x.find('h4')
		temp = stat.get_text()
		postures.append(temp)
		#f.write(temp + '\n')
		# Print campuses
		campus = x.find_all('li')
		for y in campus:
			temp = y.get_text()
			temp = temp[:-2]
			postures.append(temp)
			#f.write(temp + '\n')
	#f.close()
	print(postures)
	return postures
pitt_posture()
