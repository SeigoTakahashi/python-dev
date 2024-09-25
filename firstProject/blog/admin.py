from django.contrib import admin
from blog.models import Category, BlogPost

admin.site.register(Category)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id','title','user','category','image','posted_id')
    list_display_links = ('title','user')

admin.site.register(BlogPost, BlogPostAdmin)