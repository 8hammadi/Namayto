import requests
from bs4 import BeautifulSoup
import json
ddata=json.loads(open("0.json").read())


for k in range(len(ddata)):
	try:
		data=json.loads(open("%d.json"%(k+1)).read())
	except:
		print("error")
		continue
	for j in range(len(data)):
		print(k,j)
		try:
			URL = data[j]["href"]
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

			open("P%d_%d.json"%(k+1,j+1),"w").write(json.dumps(R))
		except Exception:
			print(Exception)