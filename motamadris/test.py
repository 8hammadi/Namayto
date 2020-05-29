import requests
from bs4 import BeautifulSoup
import json
s=input("::")
data=json.loads(open("%s.json"%(s)).read())
for j in range(len(data)):
	URL = data[j]["href"]
	print(j)
	try:
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		R=[]
		i=1
		soup=soup.find("div",class_="entry-content")
		for li in soup.findAll('li',class_='column'):
			r=li.find("a")
			h,t=r["href"],r.get_text()
			R.append({"href":h,"title":t,"id":str(i)})
			i+=1
		open("%s_%d.json"%(s,j+1),"w").write(json.dumps(R))
	except:pass
	try:
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

		open("P%s_%d.json"%(s,j+1),"w").write(json.dumps(R))
	except:
		print("error")