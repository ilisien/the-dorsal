from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from articles.models import Article
from globals import get_global_context

def redirect_to_home(request):
    return redirect('home/')

def index(request):
    published_articles = Article.objects.filter(published=True)
    scitech_articles = published_articles.filter(section=Article.Section.AT_SCITECH).order_by('-pub_date')[:3]
    pittsburgh_articles = published_articles.filter(section=Article.Section.IN_PITTSBURGH).order_by('-pub_date')[:3]    
    politics_articles = published_articles.filter(section=Article.Section.POLITICS).order_by('-pub_date')[:3]
    tech_articles = published_articles.filter(section=Article.Section.TECHNOLOGY).order_by('-pub_date')[:3]
    sports_articles = published_articles.filter(section=Article.Section.SPORTS).order_by('-pub_date')[:3]
    recent_nonprioritized = published_articles.order_by('-pub_date').values_list('pk',flat=True)[:20]
    recent_articles = published_articles.filter(pk__in=list(recent_nonprioritized)).order_by('-priority')

    context = {
        'scitech_articles':scitech_articles,
        'pittsburgh_articles':pittsburgh_articles,
        'politics_articles':politics_articles,
        'tech_articles':tech_articles,
        'sports_articles':sports_articles,
        'recent_articles':recent_articles,
    }
    context.update(get_global_context())
    print(str(context))
    return render(request,'home/index.html', context)

def contact(request):
    pass

def about(request):
    pass