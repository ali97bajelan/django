from django.conf.urls import  include, url
from django.urls import path

from django.views.generic import ListView,TemplateView
from .views import hello,helloo,sendSimpleEmail,login,saveProfile,formView,logout
from .models import Dreamreal
urlpatterns = [
    url(r'^hello/(\d+)/', hello, name = 'hello'),
    url(r'^helloo/', helloo, name = 'helloo'),
    url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',sendSimpleEmail , name = 'sendSimpleEmail'),
    url(r'^dreamreals/', ListView.as_view(model = Dreamreal,template_name = "dreamreal_list.html")),
    url(r'^connection/',formView, name = 'loginform'),
    url(r'^login/', login, name = 'login'),
    url(r'^logout/', logout, name = 'logout'),
    url(r'^profile/',TemplateView.as_view(template_name = 'profile.html')), 
    url(r'^saved/', saveProfile, name = 'saveProfile'),
]

#
#url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
