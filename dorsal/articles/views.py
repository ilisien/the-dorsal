from django.shortcuts import render
from articles.models import Article, published_articles
import datetime
from urllib.parse import unquote
from globals import get_global_context

def image_to_caption(image):
    if (image.caption != None) and (image.caption != ""):
        caption_string = f"{image.caption} - "
    else:
        caption_string = ""
    
    if image.date_taken != None:
        date_string = f" on {image.date_taken.strftime('%A, %B %-d, %Y').lower()}"
    else:
        date_string = ""

    return f'<span class="image-caption">{caption_string}<a href="/staff/{f"{image.photographer.user.first_name.lower()}_{image.photographer.user.last_name.lower()}"}/"> taken by <span class="colored-link">{image.photographer}</span></a>{date_string}</span>'

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

    author_articles = published_articles.filter(author=article.author).exclude(id=article.id).order_by('-pub_date')[:5]
    context["author_articles"] = author_articles
    context["title_image_caption"] = image_to_caption(article.title_image)

    print(author_articles)

    context.update(get_global_context())

    return render(request,'articles/article.html', context)