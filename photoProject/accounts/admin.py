from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):				
	list_display = ('id', 'username', 'birthday', 'date_joined', 'is_superuser')
	list_display_links = ('id', 'username')

admin.site.register(CustomUser, CustomUserAdmin)