from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bloggers',views.BloggerListView.as_view(),name='bloggers'),
    path('all',views.PostListView.as_view(),name='all'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('addComment/<int:pk>',views.addComment,name='add-comment'),
]
