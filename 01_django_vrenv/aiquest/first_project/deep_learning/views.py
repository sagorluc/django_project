from django.shortcuts import render
from django.http import HttpResponse as hr
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def dp_learning(request):
    # return hr('<h1>this is deep_learning apps</h1>')
    return render(request,'deep_learning/deep_learning.html')

def author_registration(request):
    if request.method == 'POST':
        frm = UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = UserCreationForm()
    return render(request, 'deep_learning/auth_registration.html', {'form': frm})
