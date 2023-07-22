from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
def abt_us(request):
    #return hr('<h1>this is about_us app</h1>')
    return render(request,'about.html')