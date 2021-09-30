from django.contrib import admin

# Register your models here.
from .models import Post, Person,Username,Picture,Video,Bio,Name

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Username)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Bio)
admin.site.register(Name)
