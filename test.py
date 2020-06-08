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
#https://graph-video.facebook.com/v6.0/%s/videos?access_token=%s
fburls={
	"102979258096775":"https://graph-video.facebook.com/v6.0/109965260746701/videos?access_token=EAANUZAFSg360BAF9laQAgGGZA9BnC9lp5ZCOTGeTZAR3nHuwlKMt3lS4A4dpp7rvASxKRWZAgcg7AsKyyuGahxpHSNBzZCc0xZBqbLttZBvU5gjlm8YnWhJV5IGGYQxEDg2Ku71B2wi1drXTZCZAIo6ukxO38nKpPnaZAxksP7ZBeTJqhLCcRHdJJyCnInm8JeMSLvkZD",	
	"113173553756637":"https://graph-video.facebook.com/v6.0/106218534461048/videos?access_token=EAAC2XG3w6tgBAHtobsOoVGYXlhMZC6dEblhLyN8LX2nyjBhjDLwHT5I6fkmiKH7VxQ2QXaLBx5hrEfuvtBNS5NMkqgfUtLtZB7Q5bZCrtsolmZB4kipwROiGGXakjKyR3tQupZB4erbgq28ubS7vtedrBoZBIUibw8QagNswDPVO7jxUfnZCJpvnQ5RwUJpUekZD"
}
id="106218534461048"
a="EAAC2XG3w6tgBAHtobsOoVGYXlhMZC6dEblhLyN8LX2nyjBhjDLwHT5I6fkmiKH7VxQ2QXaLBx5hrEfuvtBNS5NMkqgfUtLtZB7Q5bZCrtsolmZB4kipwROiGGXakjKyR3tQupZB4erbgq28ubS7vtedrBoZBIUibw8QagNswDPVO7jxUfnZCJpvnQ5RwUJpUekZD"