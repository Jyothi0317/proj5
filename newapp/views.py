from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("this is views of newapp")

def home(request):
    return render(request,"newapp/home.html",{'name':"name is jyothi"})

def child(request):
    return render(request,"child.html")
