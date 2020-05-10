# httpResponse 방식(밑의 코드는 주석처리됨)
"""
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")
"""


# render 방식
from django.shortcuts import render

def index(request):
    return render(request,'index.html')