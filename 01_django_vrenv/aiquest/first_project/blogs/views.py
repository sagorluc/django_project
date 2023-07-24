from django.shortcuts import render
from django.http import HttpResponse as hr
from blogs.forms import Teacher_registration

# Create your views here.
def blog_first(request):
    #return hr('<h1>this is first blog page</h1>') 
    return render(request,'blogs/blogs.html') 

def show_forms_data(request):
    fm = Teacher_registration()
    fm.order_fields(field_order = ['email','first_name', 'last_name']) # order maintains
    return render(request,'blogs/forms.html', {'form': fm})