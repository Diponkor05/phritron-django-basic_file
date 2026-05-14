from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("<h1>WELCOME My Webpage</h1>")
def usersid(request):
    return HttpResponse("<h1>user id cheak</h1>")

