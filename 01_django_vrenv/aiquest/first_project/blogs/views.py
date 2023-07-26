from django.shortcuts import render
from django.http import HttpResponse as hr
from blogs.forms import Teacher_registration

# Create your views here.
def blog_first(request):
    #return hr('<h1>this is first blog page</h1>') 
    return render(request,'blogs/blogs.html') 

def show_forms_data(request):
    if request.method == 'POST':
        fm = Teacher_registration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
    else:
        fm = Teacher_registration()
        print('This is get area')

    #fm.order_fields(field_order = ['email','first_name', 'last_name']) # order maintains
    return render(request,'blogs/forms.html', {'form': fm})