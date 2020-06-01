import requests
from bs4 import BeautifulSoup
import json

URL="https://easybookpdf.blogspot.com/2020/05/livre-methodix-analyse-300-methodes-250.html"	
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
r=soup.findAll(class_="separator")
a=r[-1].find("a")
print(a["href"])