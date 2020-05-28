# https://www.kutub-pdf.net/
# title="hello world"
# site = "https://www.kutub-pdf.net/"
# url = "https://www.kutub-pdf.net/search?q=%s" % (title)
# html = requests.get(url)
# parse = BeautifulSoup(html.text)
# for i in parse.find("p"):
#   a_url = i["href"]
#   app_url = site + a_url + "/download?from=details"
#   html2 = requests.get(app_url)
#   parse2 = BeautifulSoup(html2.text)
#   for link in parse2.find_all("a", id="download_link"):
#     print("+++++",link)
#     # send_file(link["href"],recipient_id,id_page)
import requests
from bs4 import BeautifulSoup
z = "https://www.hespress.com/faits-divers/472824.html"
html3 = requests.get(z)
parse3 = BeautifulSoup(html3.text)
r = parse3.find(id="article_body").findAll("p")
s = ""
print(r)
print(s)