import os
import json
k=0	
for i in os.listdir("motamadris/"):
	if i[0]=="P":
		f=json.loads(open("motamadris/"+i,"r").read())
		for v in f:
			if "//youtu" in v['href']:
				k+=1
				print(v['href'])

print(k)