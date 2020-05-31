# import json
# import pyrebase

# config={   "apiKey": "AIzaSyD7ZDxaRHJ9BO6Q6Ux-JMaa7cwmFqBeDhg",
#   "authDomain": "monstre-d44ed.firebaseapp.com",
#     "databaseURL": "https://monstre-d44ed.firebaseio.com",
#     "projectId": "monstre-d44ed",
#     "storageBucket": "monstre-d44ed.appspot.com",
#     "messagingSenderId": "345162020837",
#     "appId": "1:345162020837:web:95747eff9b6027a528610c",
#     "measurementId": "G-8V8X0GRBV0"}

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()

# r=db.child("namayto2/audios").get().val()
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)





