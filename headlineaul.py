import requests
import json
import datetime
from bs4 import BeautifulSoup

mydict = {}

currentDT = datetime.datetime.now()
page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser');
all = []

for headline in obj.find_all('div',class_='teaser_conten1'):
	a = json.dumps(headline.find('h1').text)
	b = json.dumps(headline.find('h2').text)
	c = json.dumps(headline.find('div', class_='date').text)
	mydict['Kategori']=a
	mydict['Judul']=b
	mydict['Waktu']=c
  mydict['Waktu_skrg']=currentDT.strftime("%d %b %Y %H:%M:%S")

	all.append( dict(mydict))
dictweb = all
print(mydict)
with open('headlineaul.json', 'w') as file:
	json.dump(dictweb, file, indent=4)
