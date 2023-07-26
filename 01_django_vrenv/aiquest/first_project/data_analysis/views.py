from django.shortcuts import render
from django.http import HttpResponse as hr
from django.views import View

# Create your views here.
def data_ana(request):
    #return hr('<h1>this is data_analysis app</h1>')
    
    return render(request,'data_analysis/data_analysis.html')


# create class based views
class Data_Analysis(View):
    def get(self,request):
        return render(request, 'data_analysis/class_view.html')
    
