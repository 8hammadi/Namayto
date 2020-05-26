import requests

access="EAAHn7jFl5X4BAGTRYuQq6AyYHZAXmqU75e17ELN5ouCagnY9iPAPVNUtON5egkpeXn8w0nj4RtftDqo0wAz98Po7cjMA3yYeDC1xd5N17EiDZAFOpg50g2vCioYu855SSqg1a1YshVRVkzkADejzJQUICaBJR6COUkMpfBagZDZD"
id="102979258096775"
a="https://download.apkpure.com/b/APK/YXBwLmJ1enouc2hhcmVfMzI4MDJfMzRmNjYzMDc?_fn=SGVsbyBEaXNjb3ZlciBTaGFyZSBDb21tdW5pY2F0ZV92My4yLjguMDJfYXBrcHVyZS5jb20uYXBr&as=67e4ea040d7cbd3e27b67e6a7c8b74ea5ec6c464&ai=1494118148&at=1590084588&_sa=ai%2Cat&k=113d44d3d80636105b5b3751c24d72a05ec966ec&_p=YXBwLmJ1enouc2hhcmU&c=1%7CSOCIAL%7CZGV2PUhlbG8lMjBIb2xkaW5ncyUyMExpbWl0ZWQmdD1hcGsmcz00MDkxMzI2OSZ2bj0zLjIuOC4wMiZ2Yz0zMjgwMg"


def test(url,title):
  print(url,title)
  videoName=title
  videoDescription=title
  videoUrl=url
  payload = {'name': '%s' %(videoName), 'description': '%s' %(videoDescription), 'file_url': '%s' %(videoUrl)}
  flag = requests.post('https://graph.facebook.com/v7.0/%s/files?access_token=%s'%(id,access)
, data=payload).json()
  print(flag)
1
test(a,"test")