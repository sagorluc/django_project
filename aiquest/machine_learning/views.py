from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
def machine(request):
    return hr('Welcome to Django framework.')
