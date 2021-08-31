from django.contrib import admin

# Register your models here.
from .models import Post, Blogger, Comment

admin.site.register(Post)
admin.site.register(Blogger)
admin.site.register(Comment)
#admin.site.register(User)
