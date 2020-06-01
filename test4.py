import requests
from bs4 import BeautifulSoup
import json
sss="15_9_13"
URL="http://exo7.emath.fr/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
r=soup.findAll('div',class_="fictitre")
R=[]
for i in r:
	rr=i.find("a")
	href=rr["href"]
	if "pdf" in href:
		t=rr.getText()
		h=URL+rr["href"]
		R.append({
			"title":t,
			"href":h
			})
URL="http://exo7.emath.fr/"
page = requests.get("http://exo7.emath.fr/prof.html")
soup = BeautifulSoup(page.content, 'html.parser')
r=soup.findAll('div',class_="fictitre")

for i in r:
	rr=i.find("a")
	href=rr["href"]
	if "pdf" in href:
		t=rr.getText()
		h=URL+rr["href"]
		R.append({
			"title":t,
			"href":h
			})
a=open("P16.json","w")
import json
a.write(json.dumps(R))
a.close()