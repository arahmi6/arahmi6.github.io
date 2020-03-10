import requests
import json
import datetime
from bs4 import BeautifulSoup

mydict = {}

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser');
all = []

for headline in obj.find_all('div',class_='teaser_conten1'):
	x = json.dumps(headline.find('h1').text)
	y = json.dumps(headline.find('h2').text)
	z = json.dumps(headline.find('div', class_='date').text)
	mydict['Kategori']=x
	mydict['Judul']=y
	mydict['Waktu']=z

	all.append( dict(mydict))
dictweb = all
print(mydict)
with open('headlineaul.json', 'w') as file:
	json.dump(dictweb, file, indent=4)
