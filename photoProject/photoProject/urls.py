from django.contrib import admin
from django.urls import path,include
from photo.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/',include('accounts.urls')),
    path('photo/',include('photo.urls')),
    path('admin/', admin.site.urls),
]