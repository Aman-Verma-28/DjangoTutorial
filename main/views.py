from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello world!!</h1>")  #html goes here which can be viewed from the website

def signup(response):
    return HttpResponse("Welcome to the signup page")

def user(response):
    return HttpResponse("<h1> User page </h1>")

def v1(response):
    return HttpResponse("inside v1")

def index2(request):
    return render(request,"index.html",{"name":"Akash","port":8080})

def add(request):
    num1=request.POST['num1']  # Whenever you want to submit data use POST, fetch data use GET
    num2=request.POST['num2']
    res = int(num1)+int(num2)
    return render(request,"result.html",{"val":res})
