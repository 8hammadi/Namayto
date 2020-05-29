import requests
from bs4 import BeautifulSoup
import json
sss="15_9_13"
ddata=json.loads(open("%s.json"%(sss)).read())
for k in range(len(ddata)):
	data=json.loads(open("%s_%d.json"%(sss,k+1)).read())
	for j in range(len(data)):
		URL = data[j]["href"]
		print(k,j)
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		soup=soup.findAll("div",class_="table-responsive")
		R=[]
		i=1
		for s in soup:
			for r in s.findAll('tr'):
				try:R.append({"href":r.find("a")["href"] ,"title":r.find("td").getText()})
				except:pass
				i+=1
		f=open("P%s_%d_%d.json"%(sss,k+1,j+1),"w")
		f.write(json.dumps(R))
		f.close()
		# try:
		# 	page = requests.get(URL)
		# 	soup = BeautifulSoup(page.content, 'html.parser')
		# 	R=[]
		# 	i=1
		# 	soup=soup.find("div",class_="entry-content")
		# 	for li in soup.findAll('li',class_='column'):
		# 		r=li.find("a")
		# 		h,t=r["href"],r.get_text()
		# 		R.append({"href":h,"title":t,"id":str(i)})
		# 		i+=1
		# 	open("%s_%d_%d.json"%(s,k+1,j+1),"w").write(json.dumps(R))
		# except:pass
		# try:
