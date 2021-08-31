from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-date']

    #comments = models

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Blogger(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=100)
    #posts = models.One

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):  # TODO
        return f'{self.author} on {self.post.title}'
