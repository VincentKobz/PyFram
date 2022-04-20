import json
from django.http import HttpResponse
from django.shortcuts import render
from PyService.parse import parser

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def calcul(request):
    print("test")
    body = request.body.decode('utf-8')
    print(body)
    body = json.loads(body)
    result = parser(body['expression'])
    print(result)
    return HttpResponse(result)
