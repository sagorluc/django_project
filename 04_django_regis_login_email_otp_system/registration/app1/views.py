from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .forms import HomeForm

# Create your views here.
def home(request):  
    if request.method == 'POST':
        frm = HomeForm(request.POST)
        if frm.is_valid():
            id = request.POST.get('id')
            name = request.POST.get('name') 
            from_email = request.POST.get('from_email')     
            message = request.POST.get('message') 
            # print(id, name, from_email, message)
            # print(frm.cleaned_data) 
            
            # send email
            send_mail(
                'Hi' + ' ' + name,
                message,
                from_email,              
                ['mdsagorluc@gmail.com', 'redmiolld@gmail.com']
            )        

            return render(request, 'home.html', {'forms': frm,
                                                 'id': id,
                                                 'name': name,
                                                 'from_email': from_email,
                                                 'message': message})
    else:
        frm = HomeForm()
    return render(request, 'home.html', {'forms': frm})

def signup(request):
    # GET THE DATA FORM USER 
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        
        if password != repassword:
             messages.error(request, 'Password does not matched!!')
             return redirect('signup')
        
        # put into the (database) admin panel
        my_user = User.objects.create_user(username, email, password)
        my_user.save()
        messages.success(request, 'user creation has been successfully!') # message will show in the admin panel
        return redirect('signin')
       
        
    return render(request, 'signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # checking the authentication of username, password with database username, password
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Loged In Successfully!!!')
            return redirect('home')
        else:
           messages.error(request, 'Username or Password Worng')
    
    return render(request, 'signin.html')

def logoutt(request):
    logout(request)
    messages.success(request, 'You Have LogOut Successfullly!!!')
    return redirect('signin')
