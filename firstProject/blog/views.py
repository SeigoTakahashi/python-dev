from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from blog.models import BlogPost

class IndexView(ListView):
    template_name = 'blog/index.html'
    queryset = BlogPost.objects.order_by('-posted_id')
    context_object_name = 'orderby_records'
    paginate_by = 2


class PostArticleView(TemplateView):
    template_name = 'blog/create_post.html'

class DetailArticleView(TemplateView):
    template_name = 'blog/detail_article.html'




def edit_article(request, id):
    return HttpResponse(f'記事:{id}番目を編集します。')