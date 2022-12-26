from django.shortcuts import render
from articles.models import Article
import datetime
from urllib.parse import unquote
from globals import get_global_context

def article(request, article_id=None, year=None, month=None, day=None, article_title=None):
    if article_id != None:
        article = Article.objects.get(id=article_id)
    else:
        article = Article.objects.get(url_encoded_title=article_title, pub_date__date=datetime.date(year, month, day))
    if article.published:
        context = {
            "article":article
        }        
    else:
        pass
    context.update(get_global_context())


    return render(request,'articles/article.html', context)