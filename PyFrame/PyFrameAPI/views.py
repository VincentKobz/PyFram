import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from PyService.parse import parser

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def calcul(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)
    result = parser(body['expression'])
    print("Result: " + str(result))
    if result == None:
        return HttpResponse(JsonResponse({"result": "Invalid expression"}), content_type="application/json")
    return HttpResponse(JsonResponse({"result": str(result)}), content_type="application/json")

def home(request):
    return render(request, 'index.html')
