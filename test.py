import os
import json
k=0	
R=[]
for i in os.listdir("motamadris/"):
	if i[0]=="P":
		f=json.loads(open("motamadris/"+i,"r").read())
		for v in f:
			if "//youtu" in v['href']:
				k+=1
				print(v['href'])
				R.append(v['href'])
				
print(k)
id="106218534461048"
a="EAAC2XG3w6tgBAHtobsOoVGYXlhMZC6dEblhLyN8LX2nyjBhjDLwHT5I6fkmiKH7VxQ2QXaLBx5hrEfuvtBNS5NMkqgfUtLtZB7Q5bZCrtsolmZB4kipwROiGGXakjKyR3tQupZB4erbgq28ubS7vtedrBoZBIUibw8QagNswDPVO7jxUfnZCJpvnQ5RwUJpUekZD"