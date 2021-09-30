from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .models import Person, Username, Bio, Name, Website, Post, Picture, Video
from .forms import SearchUsernameForm
from .insta import login, get_info

# Create your views here.


class PeopleListView(generic.ListView):
    """Generic class-based list view for a list of bloggers."""
    template_name = 'page/people_list.html'
    model = Person
    paginate_by = 15


class PersonDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Person


def addPage(request):
    #post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        searchForm = SearchUsernameForm(request.POST)
        if searchForm.is_valid():
            bot = login(user='ali.bajelan')
            profile = get_info(bot, searchForm.cleaned_data['username'])

            page = Person(userid=profile['userid'],
                          no_followers=profile['no_followers'], no_followings=profile['no_followings'])
            page.save()

            person = Person.objects.get(userid=profile['userid'])  # =page ?

            username = Username(
                username=searchForm.cleaned_data['username'], owner=person)
            username.save()

            name = Name(name=profile['name'], owner=person)
            name.save()

            bio = Bio(bio=profile['bio'], owner=person)
            bio.save()
            if not profile['url'] is None:
                url = Website(website=profile['url'], owner=person)
                url.save()

    else:
        return render(request, 'page/search_username.html', context={'form': SearchUsernameForm})

    return redirect('people')
