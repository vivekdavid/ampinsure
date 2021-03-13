import tempfile
import requests
from werkzeug.utils import secure_filename
from flask import Flask
from flask import request 
from flask import redirect

whitelist = ['http://www.teleshinsurance.ca','https://www.teleshinsurance.ca', 'http://www.teleshinsurance.ca.cdn.ampproject.org', 'https://www.teleshinsurance.ca.cdn.ampproject.org', 'http://www.teleshinsurance.ca.amp.cloudflare.com', 'https://www.teleshinsurance.ca.amp.cloudflare.com','https://cdn.ampproject.org']

def sendEmail(request): 
    def add_cors_headers(response):
        r = request.referrer[:-1]
        if r in white:
            response.headers.add('Access-Control-Allow-Origin', r)
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
            response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
            response.headers.add('Access-Control-Allow-Headers', 'Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')      
         return response   


    # This code will process each non-file field in the form
    fields = {}
    data = request.form.to_dict()
    for x in data:
        fields[x] = data[x]
    for name in data: 
        name = data["name"]
    for phone in data:
        phone = data["phone"]
    for date in data:
        date = data["date"] 
    for smoke in data:      
        smoke = data["smoke"] 

    requests.post("https://api.mailgun.net/v3/www.vivlaw.ca/messages",
    auth=("api", ""),
    data={"from": "Teleshinsurance Contact Form <mailgun@vivlaw.ca>",
    "to": ["vivekdavidv@gmail.com", "cteleshlaw@gmail.com",],
    "subject": "Hello",
    "text": "NAME: " +  name + " -- " +"PHONE: " + phone + "--" + "DATE OF BIRTH :" + date  + "--" + "SMOKER :" + smoke })
    return "ok"
