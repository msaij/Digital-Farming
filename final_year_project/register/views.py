from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import auth, User
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import token_generator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from userprofile.views import profile

# Create your views here.


def signup(request):
    if request.method == "GET":
        return render(request, 'register/signup.html')
    else:

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request,'email already registered')
            return redirect('signup')
        user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                        last_name=lastname, email=email)
        user.is_active = False
        user.save()
        uidb64=urlsafe_base64_encode(force_bytes(user.pk))
        token=token_generator.make_token(user)
        domain = get_current_site(request).domain
        link=reverse('activate',kwargs={
            'uidb64':uidb64,'token':token
        })
        url='http://'+domain+link
        email_body = 'hiii ' +str(user.username).title()+'! Please verify your account.\n'+url
        EmailMessage(
            'Activate Your Account',
            email_body,
            'Digital Farming',
            [email]
        ).send(fail_silently=False)
        #return HttpResponse(zip(locals().keys(),locals().values()))
        return redirect('home')


def activate(request,uidb64,token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:user=None
    if user is not None and token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('login')
    else:raise Http404("Poll does not exist")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if user.is_active==False:return render(request, 'register/login.html',{'msg':'Activate your account first'})
            return redirect('home')
        else:
            messages.info(request,'incorrect username or password')
            return render(request, 'register/login.html')


    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')

def passreset(request):
    user = auth.authenticate(username=request.user.username, password=request.POST['cpassword'])
    if user is not None:
        npass=request.POST['npassword']
        rnpass=request.POST['rnpassword']
        if npass==rnpass:
            u = User.objects.get(username=request.user.username)
            u.set_password(npass)
            u.save()
            update_session_auth_hash(request, u)
    return profile(request)