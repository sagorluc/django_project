from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
def blog_first(request):
    #return hr('<h1>this is first blog page</h1>') 
    return render(request,'blogs/blogs.html') 
