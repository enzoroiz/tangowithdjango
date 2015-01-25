from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!<br/><a href=\"/rango/about\">About page</a>")

def about(request):
    return HttpResponse("Rango says here is the about page.<br/>This tutorial has been puttogether by Enzo Roiz, 2161561<br/><a href=\"/rango\">Rango home page</a>")