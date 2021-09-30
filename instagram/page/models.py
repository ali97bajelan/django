from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
# Create your models here.

# TODO on_delete


class Bio(models.Model):
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    bio = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}: {}".format(self.owner.username_set.all()[0], self.bio)


class Username(models.Model):
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.username


class Name(models.Model):
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

# TODO URLField


class Website(models.Model):
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    website = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.website


class Person(models.Model):
    userid = models.CharField(max_length=20, unique=True)
    date = models.DateTimeField(auto_now=True)
    no_followers = models.IntegerField(validators=[MinValueValidator(0)])
    no_followings = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return "{} ({})".format(self.username_set.all()[0], self.userid)

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])


class Post(models.Model):
    author = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return '{} post {}'.format(self.owner.__str__(), self.date)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Picture(models.Model):
    image = models.ImageField()
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    PIC_TYPE = (
        ('i', 'Identifier'),
        ('p', 'Post'),
        ('s', 'Story'),
    )

    type = models.CharField(
        max_length=1,
        choices=PIC_TYPE,
        blank=False,
        default='i',
        help_text='Upload image for')

    def __str__(self):
        return '{} {} {}'.format(self.owner.__str__(), self.type, self.date)

    def get_absolute_url(self):
        return reverse('picture-detail', args=[str(self.id)])


class Video(models.Model):
    video = models.FileField(upload_to='videos_uploaded', validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    VID_TYPE = (
        ('p', 'Post'),
        ('s', 'Story'),
    )

    type = models.CharField(
        max_length=1,
        choices=VID_TYPE,
        blank=False,
        default='p',
        help_text='Upload video for')

    def __str__(self):
        return '{} {} {}'.format(self.owner.__str__(), self.type, self.date)

    def get_absolute_url(self):
        return reverse('video-detail', args=[str(self.id)])
