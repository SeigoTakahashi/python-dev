from django.contrib import admin
from blog.models import Category, BlogPost

admin.site.register(Category)
admin.site.register(BlogPost)