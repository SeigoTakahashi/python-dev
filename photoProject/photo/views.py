from django.views.generic import TemplateView, ListView, DetailView,CreateView
from photo.models import PhotoPost
from .forms import SearchForm,PhotoPostForm
from django.db.models import Q
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photo_list'
    paginate_by = 4
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
    def get_queryset(self):
        searchForm = SearchForm(self.request.GET)
        keyword = ''
        if searchForm.is_valid():
            keyword = searchForm.cleaned_data.get('key')
        queryset = PhotoPost.objects.filter(Q(title__contains=keyword) | Q(comment__contains=keyword)).order_by('-posted_at')
        return queryset
    

class PostPhotoView(CreateView):
    model = PhotoPost
    template_name = 'photo/post_photo.html'
    form_class = PhotoPostForm
    success_url = reverse_lazy("photo:index")

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
