from django.views.generic import TemplateView, ListView, DetailView
from photo.models import PhotoPost

class IndexView(ListView):
    template_name = 'photo/index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    context_object_name = 'photo_list'
    paginate_by = 4

class PostPhotoView(TemplateView):
    template_name = 'photo/post_photo.html'

class MyPageView(TemplateView):
    template_name = 'photo/mypage.html'

class CategoryView(TemplateView):
    template_name = 'photo/index.html'

class UserListView(TemplateView):
    template_name = 'photo/index.html'

class DetailPhotoView(DetailView):
    template_name = 'photo/detail.html'
    model = PhotoPost
    pk_url_kwarg = 'id'
