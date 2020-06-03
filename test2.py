# import requests
# from bs4 import BeautifulSoup
# import json

# URL="https://easybookpdf.blogspot.com/2020/05/livre-methodix-analyse-300-methodes-250.html"	
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# r=soup.findAll(class_="separator")
# a=r[-1].find("a")
# print(a["href"])

from instapy_cli import client

username = 'mc288772a@gmail.com'
password = '@123456789@'
video = 'namayto.jpg'
text = 'Namayto' + '\r\n' + ' #hash #tag #now'

with client(username, password) as cli:
    cli.upload(video, text)