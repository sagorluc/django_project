from django.shortcuts import render
from django.http import HttpResponse as hr
from about_us.models import Teacher

# Create your views here.
def abt_us(request):
    #return hr('<h1>this is about_us app</h1>')
    return render(request,'about/about.html')

def teacher_info(request):
    teach = Teacher.objects.all()
    
    return render(request,'about/teach.html',{'teac': teach} )