from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from time import sleep
driver = webdriver.Chrome()

from core import *

title,id2,id_page="سلام","278435009984417","102979258096775"
url = "https://www.kutub-pdf.net"
driver.get(url)
r=driver.find_element_by_name("q")
r.send_keys(title)
driver.find_element_by_class_name("menu-button").click()
sleep(5)
parse = BeautifulSoup(driver.page_source)
Results=parse.findAll("a",class_="gs-title")
i=Results[0]
print(i.getText(),id2,id_page)
driver.get(i["href"])
html=driver.page_source
parse = BeautifulSoup(driver.page_source)
T=parse.findAll("a",class_="button-radius")
for t in T:
	if "downloading" in str(t):
		driver.get(url+t["href"])
		driver.get(url+t["href"])
		html=driver.page_source
		parse = BeautifulSoup(driver.page_source)
		pdf=parse.find(id="download")["href"]
		print(pdf,id2,id_page)

