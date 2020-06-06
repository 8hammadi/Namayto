import requests
import json
import youtube_dl
import time
access="EAACs35XhTwwBAJxPFeb2JcMDpglSR6ZAACB2j8QdEiADNJI2hZA8NMsQeO47yNQ7R3lHtLUYhkIhWQYdHpGttYLvZApKZARZCJlIh2ROFZBGClECnWXc2eVGZC1CZAFy0w1sVee9xFeXjS1XytuPQrZBGmpWemX9b8d8IKUm1ZBbpg5wZDZD"
id="113173553756637"
fburl = 'https://graph-video.facebook.com/v6.0/%s/videos?access_token=%s' % (
    id, access)
def url_to_fb(url, title):
    videoName = title
    videoDescription = title
    videoUrl = url
    payload = {
        'name': '%s' % (videoName),
        'description': '%s' % (videoDescription),
        'file_url': '%s' % (videoUrl)
    }
    flag = requests.post(fburl, data=payload).json()
    print(flag)
    if "id" in flag:
        return flag["id"]
    else:return 0
def yt(url):
    ydl = youtube_dl.YoutubeDL()
    video = ydl.extract_info(url, download=0)
    return {'title': video['title'], 'url': video['formats'][-1]['url']}

data=json.loads(open("DATA.json","r").read())[138:300]
k=0
for d in data:
    k+=1
    try:
        R=json.loads(open("RData.json","r").read())
        print(k)#;time.sleep(2)
        if d not in R:
            y=yt(d)
            print(y["title"])
            r=url_to_fb(y["url"], y["title"])
            print(r)
            if r!=0:
                R[d]=r
            else:continue
        open("RData.json","w").write(json.dumps(R))
    except:print("error")


