import requests
import youtube_dl
access="EAAJBawiKmiwBAC9mCPIjJSCIR5n04MDLcjUECUYDs9aCQJvjuLlsGGeceiZCjOw0SqoQBkvgvcy98wrZCELnHOtOZCUvgx2ModDKZCX2jUUIIIH3SANTOUwrpyvuE9UHcZAOJdCLAQZBE4L87paH2y9EuhI1qjpKq6ZBzCqprwQtZBtNQk3MWlJz"
id = "100960198306277"
fburl = 'https://graph-video.facebook.com/v6.0/%s/videos?access_token=%s' % (
    id, access)

def yt(url):
    ydl = youtube_dl.YoutubeDL()
    video = ydl.extract_info(url, download=0)
    return {'title': video['title'], 'url': video['formats'][-1]['url']}


y = yt("https://www.youtube.com/watch?v=q8nQTNvCrjE" )

videoName = y['title']
videoDescription = y['title']
videoUrl = y['url']
payload = {
    'name': '%s' % (videoName),
    'description': '%s' % (videoDescription),
    'file_url': '%s' % (videoUrl)
}
flag = requests.post(fburl, data=payload).json()
if "id" in flag:
	print(flag)