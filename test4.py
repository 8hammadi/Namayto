from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from time import sleep
driver = webdriver.Chrome()


def book(title)
	url = "https://www.kutub-pdf.net"
	driver.get(url)
	r=driver.find_element_by_name("q")
	r.send_keys(title)
	driver.find_element_by_class_name("menu-button").click()
	sleep(10)
	parse = BeautifulSoup(driver.page_source)
	Results=parse.findAll("a",class_="gs-title")
	i=Results[0]
	print(i.getText())
	driver.get(i["href"])
	html=driver.page_source
	parse = BeautifulSoup(driver.page_source,features="lxml")
	t=parse.findAll("a",class_="button-radius")
	driver.get(url+t[2]["href"])
	driver.get(url+t[2]["href"])
	html=driver.page_source
	parse = BeautifulSoup(driver.page_source,features="lxml")
	pdf=parse.find(id="download")["href"]
	print(pdf)