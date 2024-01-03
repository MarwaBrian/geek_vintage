from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#name = input("What's your name? ")


def index(request):
    return render (request, 'eminem.html')

def lasagna(request):
    return render (request, "lasagna.html")

