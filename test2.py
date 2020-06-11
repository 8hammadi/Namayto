import os
import requests	
import re
q="life"

word=q
url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
result = requests.get(url)
html = result.text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
for each in pic_url:
    print(each)
    os.system("wget "+each)

from instabot import Bot 
bot = Bot() 
username = 'abdellatif.aithammadi@gmail.com'
password = '@15656*****9'
bot.login(username = username, 
		password = password) 
import os
i=0
for im in os.listdir():
	if im==
	try:
		bot.upload_photo(im, 
					caption ="#مسابقة_تمراز_الأولى")
	except:pass

