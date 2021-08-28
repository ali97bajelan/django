from django.shortcuts import render

from .models import Post,Blogger,User,Comment
from .forms import CommentForm
from django.views import generic
from django.views.generic.edit import CreateView
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

class BloggerDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Blogger

class PostDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Post


def addComment(request,pk):
    print(request.method)
    if request.method == 'POST':
        myCommentForm = CommentForm(request.POST)
        if myCommentForm.is_valid():
            print(myCommentForm.cleaned_data)
            comment = Comment()
            comment.text = myCommentForm.cleaned_data['text']
            comment.post = myCommentForm.cleaned_data['post']

            comment.author = myCommentForm.cleaned_data['user']
            comment.save()
            is_saved = True
    else:
        print(locals())
        return render(request,'blog/add_comment.html',locals())
        myProfileForm = CommentForm()
   
    return render(request,'blog/saved.html',locals())

'''
def bloggers_list(request):
    list_of_bloggers = Blogger.objects.all()
    data={'blogger_list':list_of_bloggers}
    return render(request,'blogger_list.html',context=data)
'''
