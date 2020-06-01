import requests
from bs4 import BeautifulSoup
import json
data=json.loads(open("17.json").read())
k=1
for d in data:
	R=json.loads(open("P17_%d.json"%(k)).read())
	for i in range(len(R)):
		try:
			URL=R[i]["href"]
			page = requests.get(URL)
			soup = BeautifulSoup(page.content, 'html.parser')
			r=soup.findAll(class_="separator")
			a=r[-1].find("a")
			print(a["href"])
			R[i]["href"]=a["href"]
		except:pass
	a=open("P17_%d.json"%(k),"w")
	import json
	a.write(json.dumps(R))
	a.close()
	k+=1
