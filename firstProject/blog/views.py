from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'blog/index.html'


class PostArticleView(TemplateView):
    template_name = 'blog/create_post.html'

class DetailArticleView(TemplateView):
    template_name = 'blog/detail_article.html'




def edit_article(request, id):
    return HttpResponse(f'記事:{id}番目を編集します。')