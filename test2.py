from instapy_cli import client

username = '****'
password = '***'
video = 'namayto.jpg'
text = 'Namayto' + '\r\n' + ' #hash #tag #now'

with client(username, password) as cli:
    cli.upload(video, text)