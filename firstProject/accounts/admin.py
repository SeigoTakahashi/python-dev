from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):				# CustomUserAdminクラスを追加
    list_display = ('id', 'username', 'kana', 'is_staff')
    list_display_links = ('id', 'username', 'kana')
 
 # Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)


