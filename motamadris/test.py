import requests
from bs4 import BeautifulSoup
import json
dddata=json.loads(open("0.json").read())

for a in range(len(dddata)):
	try:ddata=json.loads(open(str(a+1)+".json").read())
	except:
		print("error")
		continue
	for k in range(len(ddata)):
		try:data=json.loads(open("%d_%d.json"%(a+1,k+1)).read())
		except:
			print("error")
			continue
		for j in range(len(data)):
			print(a,k,j)
			try:
				URL = data[j]["href"]
				# page = requests.get(URL)
				# soup = BeautifulSoup(page.content, 'html.parser')
				# R=[]
				# i=1
				# soup=soup.find("div",class_="entry-content")
				# for li in soup.findAll('li',class_='column'):
				# 	r=li.find("a")
				# 	h,t=r["href"],r.get_text()
				# 	R.append({"href":h,"title":t,"id":str(i)})
				# 	i+=1
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

				open("P%d_%d_%d.json"%(a+1,k+1,j+1),"w").write(json.dumps(R))
			except:
				print("error")