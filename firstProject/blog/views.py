from datetime import datetime
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,FormView,CreateView
from blog.models import BlogPost
from .forms import SearchForm,PostForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator		
from django.contrib.auth.decorators import login_required

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

@method_decorator(login_required, name='dispatch')
class PostArticleView(CreateView):
    model = BlogPost
    template_name = 'blog/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
         # commit=FalseにしてPOSTされたデータを取得
         postdata = form.save(commit=False)
         # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
         postdata.user = self.request.user
         # 投稿データをデータベースに登録
         postdata.save()
         # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
         return super().form_valid(form)

class DetailArticleView(DetailView):
    template_name = 'blog/detail_article.html'
    model = BlogPost
    pk_url_kwarg = 'id'


def edit_article(request, id):
    return HttpResponse(f'記事:{id}番目を編集します。')

class MyPageView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'orderby_records'
    paginate_by = 4
    def get_queryset(self):
        queryset = BlogPost.objects.filter(user=self.request.user)
        return queryset
    