from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
def data_ana(request):
    #return hr('<h1>this is data_analysis app</h1>')
    
    return render(request,'data_analysis.html')
