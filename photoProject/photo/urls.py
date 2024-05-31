from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostPhotoView.as_view(), name='post_photo'),
    path('mypage/', views.MyPageView.as_view(), name='mypage'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category'),
    path('user_list/<int:id>/', views.UserListView.as_view(), name='user_list'),
    path('detail/<int:id>/', views.DetailPhotoView.as_view(), name='detail_photo'),
]