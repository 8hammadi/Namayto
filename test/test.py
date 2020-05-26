import requests

import json

access = "EAAHn7jFl5X4BAGTRYuQq6AyYHZAXmqU75e17ELN5ouCagnY9iPAPVNUtON5egkpeXn8w0nj4RtftDqo0wAz98Po7cjMA3yYeDC1xd5N17EiDZAFOpg50g2vCioYu855SSqg1a1YshVRVkzkADejzJQUICaBJR6COUkMpfBagZDZD"
id = "102979258096775"
a = "https://download.apkpure.com/b/APK/YXBwLmJ1enouc2hhcmVfMzI4MDJfMzRmNjYzMDc?_fn=SGVsbyBEaXNjb3ZlciBTaGFyZSBDb21tdW5pY2F0ZV92My4yLjguMDJfYXBrcHVyZS5jb20uYXBr&as=67e4ea040d7cbd3e27b67e6a7c8b74ea5ec6c464&ai=1494118148&at=1590084588&_sa=ai%2Cat&k=113d44d3d80636105b5b3751c24d72a05ec966ec&_p=YXBwLmJ1enouc2hhcmU&c=1%7CSOCIAL%7CZGV2PUhlbG8lMjBIb2xkaW5ncyUyMExpbWl0ZWQmdD1hcGsmcz00MDkxMzI2OSZ2bj0zLjIuOC4wMiZ2Yz0zMjgwMg"

import pyrebase
zz = "https://web.facebook.com/hamza.zahwani.395669"
config = {
    "apiKey": "AIzaSyD7ZDxaRHJ9BO6Q6Ux-JMaa7cwmFqBeDhg",
    "authDomain": "monstre-d44ed.firebaseapp.com",
    "databaseURL": "https://monstre-d44ed.firebaseio.com",
    "projectId": "monstre-d44ed",
    "storageBucket": "monstre-d44ed.appspot.com",
    "messagingSenderId": "345162020837",
    "appId": "1:345162020837:web:95747eff9b6027a528610c",
    "measurementId": "G-8V8X0GRBV0"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# db.child("namayto2/users").set([0])
def send_to_fb(message_text, recipient_id="2956725364362668"):
    params = {"access_token": access}
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

l = db.child("namaytu").get().val()




test = """
ﻋﻴﺪﻛﻢ ﻣﺒﺎﺭﻙ ﺳﻌﻴﺪ ﻟﻜﻢ ﻭﻟﻜﻞ ﺃﻓﺮاﺩ ﺃﺳﺮﻛﻢ ﻭﺃﻗﺎﺭﺑﻜﻢ ﻭﺃﺻﺪﻗﺎءﻛﻢ ﻭﺟﻴﺮاﻧﻜﻢ ﻭﻛﻞ ﺃﺣﺒﺘﻜﻢ ﻓﻲ اﻟﻠﻪ
ﺗﻘﺒﻞ اﻟﻠﻪ ﻣﻨﻜﻢ ﻭﻣﻨﻬﻢ ﺻﻴﺎﻣﻜﻢ ﻭ ﻗﻴﺎﻣﻜﻢ ﻭﺻﺎﻟﺢ ﺃﻋﻤﺎﻟﻜﻢ ﻭﻏﻔﺮ اﻟﻠﻪ ﻟﻜﻢ ﺫﻧﻮﺑﻜﻢ ﻣﺎ ﺗﻘﺪﻡ ﻭﻣﺎ ﺗﺄﺧﺮ ﻣﻨﻬﺎ ﻭﺟﻌﻠﻜﻢ اﻟﻠﻪ ﺃﺟﻤﻌﻴﻦ ﻣﻦ ﻋﺘﻘﺎء اﻟﻨﺎﺭ
ﺩﻣﺘﻢ ﺩاﺋﻤﺎ ﻣﺘﺄﻟﻴﻖ ﻭﻣﻔﺎﺗﻴﺢ ﻟﻠﺨﻴﺮ ﻭﺗﺎﺟﺎ ﻋﻠﻰ ﺭﺅﻭﺱ ﺃﻭﻃﺎﻧﻜﻢ
 
"""
for i in l:
    print(i)
    send_to_fb(test, i)
