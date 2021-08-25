from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bloggers',views.BloggerListView.as_view(),name='bloggers'),
    path('all',views.PostListView.as_view(),name='all'),

]