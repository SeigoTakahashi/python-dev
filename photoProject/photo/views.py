from django.views.generic import TemplateView, ListView, DetailView,CreateView
from photo.models import PhotoPost
from .forms import SearchForm,PhotoPostForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator		
from django.contrib.auth.decorators import login_required

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
    
@method_decorator(login_required, name='dispatch')
class PostPhotoView(CreateView):
    model = PhotoPost
    template_name = 'photo/post_photo.html'
    form_class = PhotoPostForm
    success_url = reverse_lazy("photo:index")

    def form_valid(self, form):
        postdata = form.save(commit=False)
        
        postdata.user = self.request.user
        
        postdata.save()
        
        return super().form_valid(form)

class MyPageView(ListView):
    template_name = 'photo/mypage.html'
    context_object_name = 'photo_list'
    paginate_by = 4
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = len(PhotoPost.objects.filter(user=self.request.user))
        return context
    def get_queryset(self):
        queryset = PhotoPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

class CategoryView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photo_list'
    paginate_by = 4
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
    def get_queryset(self):
        category = self.kwargs.get('category', '')
        queryset = PhotoPost.objects.filter(category__title=category).order_by('-posted_at')
        return queryset

class UserListView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photo_list'
    paginate_by = 4
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
    def get_queryset(self):
        user_id = self.kwargs.get('id', 1)
        print(f"user_id{user_id}")
        queryset = PhotoPost.objects.filter(user=user_id).order_by('-posted_at')
        return queryset

class DetailPhotoView(DetailView):
    template_name = 'photo/detail.html'
    model = PhotoPost
    pk_url_kwarg = 'id'
