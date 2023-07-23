from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
def dp_learning(request):
    # return hr('<h1>this is deep_learning apps</h1>')
    return render(request,'deep_learning/deep_learning.html')