

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):

    return HttpResponse("welcome to emobilis")

def about(request):
    return HttpResponse("about emobilis")
