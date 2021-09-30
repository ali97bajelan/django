from django.urls import path
from . import views
#    path('',views.index,name='index'),

urlpatterns = [
    path('people',views.PeopleListView.as_view(),name='people'),
    path('add',views.addPage,name='add'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),

]
