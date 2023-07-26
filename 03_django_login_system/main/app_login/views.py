
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from main import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from main import generate_token
from django.core.mail import EmailMessage, send_mail

# Create your views here.
def home(request):
    #return HttpResponse('hellow im sagor ahmed')
    return render(request, 'authentication/home.html')
    
def signup(request):
    if request.method == 'POST':
        #username = request.POST.get('username') # catch by (name) of html field
        username = request.POST['username'] # second way to do
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        
        # checking validation of username, email,password
        if User.objects.filter(username = username):
            messages.error(request, 'This username already exists!try another username')
            return redirect('home')
        
        if User.objects.filter(email = email):
            messages.error(request, 'This email already registered!')
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request,'username should not be more the 10 character!')
        
        if password != repassword:
            messages.error(request, 'password does not mached!')
            
        if not username.isalnum():
            messages.error(request, 'username should be Alpha-Numeric')
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, password)
        
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        
        # welcome email
        subject = 'Welcome to this email'
        message = 'Hellow' + ' ' + myuser.first_name + '!! \n' + 'Welcome to my email!! \n Thank yor for visition my website! \n We have also sent you a confirmation email.please click the link to confirm the email'
        from_email = settings.EMAIL_HOST_USER
        to_recived = [myuser.email]
        send_mail(subject, message, from_email, to_recived, fail_silently = True)
        
        # email address comfirmation email
        current_site = get_current_site(request)
        email_subject = 'Confirm your emil for django login!'
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'user_id': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
            
        )
        
        email.fail_silently = True
        email.send()
        
        
        messages.success(request, 'Your Account Has Been Created Successfully! We have sent you a emil to your email account.')
        return redirect('signin')
        
    #return HttpResponse('hellow im sagor ahmed from sign-up')
    return render(request, 'authentication/signup.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # checking user authentication
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/home.html', {'fname': fname})
        else:
            messages.error(request, 'Bad Credentials')
            return redirect('home')
    
    
    
    
    
    
    #return HttpResponse('hellow im sagor ahmed from sign-in')
    return render(request, 'authentication/signin.html')
    
def signout(request):
    logout(request)
    messages.success(request,  'Loged Out Successfully')
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk = uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser )
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')
        
    
