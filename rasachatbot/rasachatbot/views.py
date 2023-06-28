from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.http import JsonResponse

def home(request):
    return render(request,'home.html')

def create(request):
    sender='samriddha'
    lis=request.GET.getlist('msg')
    print(lis)
    lis=lis[0]
    print(lis)
    print(type(lis))
    message=lis
    print("sending message now...")
    r=requests.post("http://localhost:5002/webhooks/rest/webhook",json={"sender":sender,"message":message})
    for i in r.json():
        r=i['text']


    return JsonResponse(r,safe=False)