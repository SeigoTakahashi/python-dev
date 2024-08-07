from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from blog.models import BlogPost
from .forms import SearchForm

class IndexView(ListView):
    template_name = 'blog/index.html'
    # queryset = BlogPost.objects.order_by('-posted_id')
    context_object_name = 'orderby_records'
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
        queryset = BlogPost.objects.filter(title__contains=keyword).order_by('-posted_id')
        return queryset


class PostArticleView(TemplateView):
    template_name = 'blog/create_post.html'

class DetailArticleView(DetailView):
    template_name = 'blog/detail_article.html'
    model = BlogPost
    pk_url_kwarg = 'id'


def edit_article(request, id):
    return HttpResponse(f'記事:{id}番目を編集します。')