from django.contrib import admin
from django.urls import path,include
from blog.views import IndexView
from django.conf import settings									
from django.conf.urls.static import static							



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/',include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)