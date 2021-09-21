from django.shortcuts import render , HttpResponse, redirect
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from datetime import datetime
from home.models import Contact, Project
from django.contrib import messages
from django.contrib.auth.models import auth 
from django.contrib.auth.models import User 
from django.views.generic.list import ListView

# Create your views here.

def project(request):
    pro = Project.objects.all()
    context = {'pro':pro}

    return render(request,"project.html", context)

def index(request):
    # below two lines will show to project containts
    pro = Project.objects.all()
    context = {'pro':pro}
    
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contact=Contact(name=name, email=email,msg=msg ,date=datetime.today())
        contact.save()
        messages.success(request, 'your message is being send')


         #email section
        subject = 'Shantanu@<no-reply>'
        html_content =render_to_string("reply.html",{'title':'test mail','name':name})
        text_content =strip_tags(html_content)

        email=EmailMultiAlternatives(
            #subject
            "Shantanu@<no-reply>",
            #content
            text_content,
            #from email
            "shantanunimkar19@gmail.com",
            #rec_list
            [email])
        email.attach_alternative(html_content,"text/html")
        email.send()


    
    return render(request,"index.html", context)

def contact(request):
   if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contact=Contact(name=name, email=email,msg=msg ,date=datetime.today())
        contact.save()
        messages.success(request, 'your message is being send')


         #email section
        subject = 'Shantanu@<no-reply>'
        html_content =render_to_string("reply.html",{'title':'test mail','name':name})
        text_content =strip_tags(html_content)

        email=EmailMultiAlternatives(
            #subject
            "Shantanu@<no-reply>",
            #content
            text_content,
            #from email
            "shantanunimkar19@gmail.com",
            #rec_list
            [email])
        email.attach_alternative(html_content,"text/html")
        email.send()
        return render(request,".html")


def handleSignup(request):
    if request.method=="POST":
       
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['password1']
        
    # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, " Account Added Successfully")
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')
    

def handleLogin(request):
    if request.method=="POST":
        loginuser=request.POST['loginusername']
        loginpass=request.POST['loginpassword']
        
        user=auth.authenticate(username=loginuser , pass1=loginpass)

        if user is not None:
            auth.login(request , user)
            messages.success(request , "Successfully Logged In")
            return redirect('/')
        else:
            messages.success(request , "Invalid Credentials , Please try again")
            return redirect('/')
        
    return HttpResponse(request,"404 - Not Found")



def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "successfully logged out !")
        return redirect('/')
    return HttpResponse('handleLogout')
   
def dashboard(request):
    return render(request, "about.html")

def writes(request):
    return render(request,"writes.html")


