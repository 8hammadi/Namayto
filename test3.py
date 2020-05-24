import requests
access="EAAHn7jFl5X4BADxOUMqq6nguKCqTLPWas65euIZBUlbDP2k36Wm15Joh2ZBNkFVnJ44ZAIb6r7cKmJC7TfkeoZB8Fk7RDOLwt53ObFbLZBHuBpJ62dzYtMaieecC5TvfZCNcJFmlvHajt2Cp3WIj6g0RjNLe4hJ3aKHB8Mc6n4KNz2M08qtCEubAX36kZBZAZBhwZBpPgZBEeHs8gZDZD"
url="https://r2---sn-p5qlsndk.googlevideo.com/videoplayback?expire=1590196294&ei=5iPIXtiwE6Kx8gTNtpGQBg&ip=54.83.147.185&id=o-AMK9E7AutoVNfiJ9fhf2mWuiMKhLpo_pXbjkkfBaADSO&itag=18&source=youtube&requiressl=yes&mh=TY&mm=31%2C26&mn=sn-p5qlsndk%2Csn-vgqsrnek&ms=au%2Conr&mv=u&mvi=1&pl=24&vprv=1&mime=video%2Fmp4&gir=yes&clen=6923734&ratebypass=yes&dur=247.129&lmt=1575198521407565&mt=1590174288&fvip=2&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl&lsig=AG3C_xAwRgIhAMg_ktnw8Jzmhu4i9Likm1P6MCRPH2B7G8u-KUU4Vtl3AiEAwQTisPURZ7rIR79sOvkzUNDb-AnTWuVfYHIT0fw7pTE%3D&sig=AOq0QJ8wRQIgaCJyV5XcaiFy-xxnM6ysgTr5tvshUw2aiNkXH1FQ3wUCIQCJYTEpXv0mrPyO5b-PFNgOcULxYYwpKfuvTFsvnUV9gg=="
id="100960198306277"
title="test"
fburl = 'https://graph.facebook.com/v7.0/%s/files?access_token=%s'%(id,access)


print(url,title)
videoName=title
videoDescription=title
videoUrl=url
payload = {'name': '%s' %(videoName), 'description': '%s' %(videoDescription), 'file_url': '%s' %(videoUrl)}
flag = requests.post(fburl, data=payload).json()
print(flag)
