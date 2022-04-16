from django.http import HttpResponse
from django.shortcuts import render
from PyService.parse import parser

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def calcul(request, calcul_request):
    print(calcul_request)
    result = parser(calcul_request)
    print(result)
    return HttpResponse(result)
