from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'photo/index.html'

class PostPhotoView(TemplateView):
    template_name = 'photo/post_photo.html'

class MyPageView(TemplateView):
    template_name = 'photo/mypage.html'

class CategoryView(TemplateView):
    template_name = 'photo/index.html'

class UserListView(TemplateView):
    template_name = 'photo/index.html'

class DetailPhotoView(TemplateView):
    template_name = 'photo/detail.html'
