import requests
import json
sender=input()

bot_message=''

while bot_message != "Bye":
    message=input('What is your message?  ')
    print("sending message now...")
    r=requests.post("http://localhost:5002/webhooks/rest/webhook",json={"sender":sender,"message":message})


    for i in r.json():
        message=i['text']
    print(message)