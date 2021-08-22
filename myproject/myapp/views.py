import django
django.setup()
from django.shortcuts import render#, render_to_response

# Create your views here.

from django.http import HttpResponse, response
from django.template import RequestContext

import datetime
from django.core.mail import send_mail
from .forms import LoginForm , ProfileForm
from .models import Profile

def saveProfile(request):
   is_saved = False
   if request.method == 'POST':
      myProfileForm = ProfileForm(request.POST,request.FILES)
      if myProfileForm.is_valid():
         profile = Profile()
         profile.name = myProfileForm.cleaned_data['name']
         profile.picture = myProfileForm.cleaned_data['picture']
         profile.save()
         is_saved = True
   else:
      myProfileForm = ProfileForm()
   
   return render(request,'saved.html',locals())

def login(request):
   print('login',request.COOKIES)

   if  'username' in request.COOKIES:
      username = request.COOKIES['username']
   else:
      username = "not logged in"
   
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         request.session['username'] = username
   else:
      MyLoginForm = LoginForm()
   cookies = {"username" : username,'last_connection':datetime.datetime.now()}
   print('G',cookies)
   return render(request,'loggedin.html',cookies)	
   response.set_cookie('last_connection', datetime.datetime.now())
   response.set_cookie('username', username)
   return response
   #return render(request, 'loggedin.html', {"username" : username})

def formView(request):
   print('formView',request.COOKIES)
   print('formView',request.session)
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, 'login.html', {})

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")

def formView0(request):
   print('formView',request.COOKIES)
   
   if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
      username = request.COOKIES['username']
      last_connection = request.COOKIES['last_connection']
      last_connection_time = datetime.datetime.strptime(last_connection[:-7], 
         "%Y-%m-%d %H:%M:%S")
      print(last_connection_time)
      print(datetime.datetime.now())
      print((datetime.datetime.now() - last_connection_time).seconds)
      if (datetime.datetime.now() - last_connection_time).seconds < 30:
         return render(request, 'loggedin.html', {"username" : username})
      else:
         print('worked')
         del request.COOKIES['username']
         del request.COOKIES['last_connection']
         print(request.COOKIES)

         return render(request, 'login.html', {})
		
   else:
      print('not worked')
      return render(request, 'login.html', {})


def hello(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)

def helloo(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today" : today})


def sendSimpleEmail(request,emailto):
   res = send_mail(subject="hello paul", message="comment tu vas?", from_email="paul@polo.com", recipient_list=[emailto])
   return HttpResponse('%s'%res)

'''
def hello(request):
   return render(request, "myapp/template/hello.html", {})
'''