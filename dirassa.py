import requests
import json
import youtube_dl
import time
access="EAANUZAFSg360BAIlxgG5fS08orsUsMnjDb1Q4TGupvZAvhxEMvHkbYEZCitOfjtvgwjbgg2B9wskrqpw7GIfPpZCFSmZBVSCWHHcjNcKYvsC3mOKux6y29ZCJiOFs5ZAHlgampq0ZAwVprHF2BOKg8dgAWz3vGyKNySfuhOHmkLQF9lB964FuIdSZCZCkoFUdEWsgZD"
id="102979258096775"
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

data=json.loads(open("DATA.json","r").read())[1105:]
k=0
R=json.loads(open("RData.json","r").read())
for d in data:
    k+=1
    try:
        print(k);
        if d not in R:
            y=yt(d)
            print(y["title"])
            r=url_to_fb(y["url"], y["title"])
            time.sleep(10)
            print(r)
            if r!=0:
                R[d]=r
                open("RData.json","w").write(json.dumps(R))
            else:continue
    except:print("error")


