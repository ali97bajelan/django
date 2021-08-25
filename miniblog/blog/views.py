from django.shortcuts import render

from .models import Post,Blogger,User
from django.views import generic
# Create your views here.

def index(request):
    no_posts = Post.objects.all().count()
    no_blogger = Blogger.objects.all().count()
    no_user = User.objects.all().count()

    no_visits = request.session.get('no_visits', 1)
    request.session['no_visits'] = no_visits+1
    data = {'no_posts':no_posts,'no_author':no_blogger,'no_user':no_user,'no_visits':no_visits}

    return render(request,'index.html',context=data)

class BloggerListView(generic.ListView):
    """Generic class-based list view for a list of bloggers."""
    template_name = 'templates/blog/blogger_list.html'
    model = Blogger
    paginate_by = 10


class PostListView(generic.ListView):
    """Generic class-based list view for a list of posts."""
    model = Post
    paginate_by = 20


'''
def bloggers_list(request):
    list_of_bloggers = Blogger.objects.all()
    data={'blogger_list':list_of_bloggers}
    return render(request,'blogger_list.html',context=data)
'''