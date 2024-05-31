from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [ 
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostArticleView.as_view(), name='post_article'),
    path('detail/<int:id>/', views.DetailArticleView.as_view(), name='detail_article'),
    path('edit/<int:id>/', views.edit_article, name='edit_article'),
]