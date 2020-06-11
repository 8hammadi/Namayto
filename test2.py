from instabot import Bot 


bot = Bot() 
username = 'mc288772a@gmail.com'
password = '@***********@'

bot.login(username = username, 
		password = password) 

# Recommended to put the photo 
# you want to upload in the same 
# directory where this Python code 
# is located else you will have 
# to provide full path for the photo 
bot.upload_photo("ok.png", 
				caption ="magic") 


