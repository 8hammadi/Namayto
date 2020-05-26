import requests
from bs4 import BeautifulSoup
import json

URL = "https://moutamadris.ma/%d8%a7%d9%84%d9%82%d8%a7%d9%86%d9%88%d9%86-%d8%a7%d9%88%d9%84%d9%89-%d8%a8%d8%a7%d9%83/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
soup=soup.findAll("div",class_="table-responsive")
R=[]
for s in soup:
	for r in s.findAll('tr'):
		R.append({"href":r.find("a")["html"] ,"title":r.find("td").getText()})

