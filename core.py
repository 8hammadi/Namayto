from PIL import Image
from io import BytesIO
from math import *
from urllib.request import urlopen
import speech_recognition as sr
from bs4 import BeautifulSoup
import threading
from googlesearch import search
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from selenium import webdriver
import os
import time
from youtube_search import YoutubeSearch
import sys
import wikipedia
from pydub import AudioSegment
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
import random
import smtplib
from django.views import generic
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import json
import pyrebase
from googletrans import Translator
import urllib.request
import urllib.parse
import youtube_dl
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.set_window_size(1080,2000)
wikipedia.set_lang("ar")
subscription_key = os.environ["subscription_key"]
endpoint = os.environ["ENDPOINT"]
ocr_url = endpoint + "vision/v2.1/ocr"
config = json.loads(os.environ["FIREBASE_CONFIG"])
access = os.environ["PAGE_ACCESS_TOKEN"]
id = os.environ['PAGE_ID']
fburl = 'https://graph-video.facebook.com/v6.0/%s/videos?access_token=%s' % (
    id, access)
"""
pages={
    "id1":"acces1",
   "id2":"acces2"
}


"""
pages=json.loads(os.environ['PAGES'])

access_v = "EAAHn7jFl5X4BAH3fITlm37PHvVoSWIMEfaEIohFVAYImSRAcDaxVMimjuB5NOmtmzpjZCaF43Qshs4Km7qZA5o7dkCsoWAEgik2zn39JJlMY3winDHJx7c9ZBvotFRGehLLtYyWyXBFkqu1rGMNK2gjYEXo8BrMMnT3IvamWgZDZD"
id_v = "100960198306277"
fburl_v = 'https://graph-video.facebook.com/v6.0/%s/videos?access_token=%s' % (
    id_v, access_v)

VERIFY_TOKEN = "123456789"
firebase = pyrebase.initialize_app(config)
db = firebase.database()



def url_to_fb(url, title, recipient_id):
    videoName = title
    videoDescription = title
    videoUrl = url
    payload = {
        'name': '%s' % (videoName),
        'description': '%s' % (videoDescription),
        'file_url': '%s' % (videoUrl)
    }
    flag = requests.post(fburl_v, data=payload).json()
    if "id" in flag:
        send_to_fb(
            " ﺳﻴﻜﻮﻥ اﻟﻖﻳﺪﻳﻮ ﺟﺎﻫﺰا ﻋﻠﻰ ﻫﺪا اﻟﺮﺑﻂ ﺑﻌﺪ ﻗﻠﻴﻞ  https://www.facebook.com/watch/?v=%s"
            % (flag["id"]), recipient_id)
    else:
        send_to_fb("..", recipient_id)



def yt(url):
    ydl = youtube_dl.YoutubeDL()
    video = ydl.extract_info(url, download=0)
    return {'title': video['title'], 'url': video['formats'][-1]['url']}


def send_to_fb(message_text, recipient_id="2956725364362668",sender=id):
    params = {"access_token": pages[sender]}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        'recipient': {
            'id': recipient_id
        },
        'message': {
            "text": message_text,
        },
    })
    r = requests.post(
        "https://graph.facebook.com/v7.0/me/messages",
        params=params,
        headers=headers,
        data=data)
    print("RRR:",r.json())


def speech_to_text(url):
    mp4file = urlopen(url)
    with open("test.mp4", "wb") as handle:
        handle.write(mp4file.read())
    wav_audio = AudioSegment.from_file("test.mp4", format="mp4")
    wav_audio.export("test.wav", format="wav")
    r = sr.Recognizer()
    with sr.AudioFile('test.wav') as source:
        audio = r.record(source)
    command = r.recognize_google(audio, language="ar-AR")
    os.remove("test.mp4")
    os.remove("test.wav")
    return command


def trad(m, l):
    translator = Translator()
    return translator.translate(m, src='auto', dest=l).text


def send_video_to_fb(url, recipient_id="2956725364362668", title=""):
    params = {"access_token": access}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        'recipient': {
            'id': recipient_id
        },
        "message": {
            "attachment": {
                "type": "video",
                "payload": {
                    "url": url
                }
            }
        }
    })
    r = requests.post(
        "https://graph.facebook.com/v7.0/me/messages",
        params=params,
        headers=headers,
        data=data)
    # print(r.json())
    if "message_id" not in r.json():
        if recipient_id in db.child("namayto2/users").get().val() or 1:
            url_to_fb(url, title, recipient_id)
        else:
            send_to_fb("ﻓﺸﻞ اﻟﻄﻠﺐ", recipient_id)


def to_text(image_url, id):
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'language': 'unk', 'detectOrientation': 'true'}
    data = {'url': image_url}
    response = requests.post(
        ocr_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = response.json()
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info)
    t = ""
    for word in word_infos:
        t += " " + word["text"]
    send_to_fb(t, id)


def get_apk(app_name,recipient_id):
    print("**********************-+-+-",app_name,recipient_id)
    site = "https://apkpure.com"
    url = "https://apkpure.com/search?q=%s" % (app_name)
    html = requests.get(url)
    parse = BeautifulSoup(html.text)
    for i in parse.find("p"):
        a_url = i["href"]
        app_url = site + a_url + "/download?from=details"
        html2 = requests.get(app_url)
        parse2 = BeautifulSoup(html2.text)
        for link in parse2.find_all("a", id="download_link"):
            print("+++++",link)
            send_file(link["href"],recipient_id)
    send_to_fb("ادا لم تتوصل بالتطبيق فغالبا التطبيق دو حجم كبير  ",recipient_id)
def send_file(url, recipient_id):
    print("sending APK  ...",url," to ",recipient_id)
    params = {"access_token": access}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        'recipient': {
            'id': recipient_id

        },
        "message": {
            "attachment": {
                "type": "file",
                "payload": {
                    "url": url
                }
            }
        }
    })
    r = requests.post(
        "https://graph.facebook.com/v6.0/me/messages",
        params=params,
        headers=headers,
        data=data)
    print(r.json())

def test(url, title, recipient_id):
    print("posting apk ")
    videoName = title
    videoDescription = title
    videoUrl = url
    payload = {
        'name': '%s' % (videoName),
        'description': '%s' % (videoDescription),
        'file_url': '%s' % (videoUrl)
    }
    flag = requests.post(
        'https://graph.facebook.com/v6.0/%s/files?access_token=%s' % (id,
                                                                      access),
        data=payload).json()
    print(flag)
    send_to_fb(str(flag),recipient_id)


def ok(url, recipient_id="2971238896277759"):
    try:
        driver.get(url)
        png=driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
        time.sleep(2)
        im.save('screenshot.png')  # saves new cropped image
        params = {"access_token": access}
        headers = {"Content-Type": "application/json"}
        storage = firebase.storage()
        storage.child("imagesfb").put("screenshot.png")
        url1 = storage.child("imagesfb").get_url("SFNcLgpBV9OCffzjIGhlqMxRAJe2")
        data = json.dumps({
            'recipient': {
                'id': recipient_id
            },
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": url1
                    }
                }
            }
        })
        r = requests.post(
            "https://graph.facebook.com/v7.0/me/messages",
            params=params,
            headers=headers,
            data=data)
        print(r.json())
    except:
        send_to_fb("invalid url",recipient_id)


def audio(url_yt,recipient_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    video = ydl.extract_info(url_yt, download=0)
    r= video['formats'][-1]['url']
    params = {"access_token": access}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        'recipient': {
            'id': recipient_id
        },
        "message": {
            "attachment": {
                "type": "audio",
                "payload": {
                    "url": r
                }
            }
        }
    })
    r = requests.post(
        "https://graph.facebook.com/v7.0/me/messages",
        params=params,
        headers=headers,
        data=data)
    print(r.json())

def image(url_yt,recipient_id):
    params = {"access_token": access}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        'recipient': {
            'id': recipient_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url_yt
                }
            }
        }
    })
    r = requests.post(
        "https://graph.facebook.com/v7.0/me/messages",
        params=params,
        headers=headers,
        data=data)
    print(r.json())


import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

def download_baidu(word,recipient_id): 
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    html = result.text
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    for each in pic_url[:10]:
        # print(each)
        image(each,recipient_id)

def download_google(word,recipient_id):
    url = 'https://www.google.com/search?q=' + word + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    for raw_img in soup.find_all('img')[:10]:
       link = raw_img.get('src')
       # print(link)
       image(link,recipient_id)

# def MM(URL)
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     R=[]
#     for r in soup.findAll('a'):
#         h=r["href"]
#         if ".pdf" in h:
#             R.append(h)
#     return R