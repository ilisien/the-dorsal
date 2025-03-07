from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from articles.models import Article,published_articles
from globals import get_global_context
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
import os
from django.http import FileResponse

def grab_md(name):
    file = staticfiles_storage.url(f'markdown/{name}.md')[1:]
    with open(file, "r") as f:
        return f.read()

def redirect_to_home(request):
    return redirect('home/')

def index(request):
    scitech_articles = published_articles.filter(section=Article.Section.AT_SCITECH).order_by('-pub_date')[:3]
    pittsburgh_articles = published_articles.filter(section=Article.Section.IN_PITTSBURGH).order_by('-pub_date')[:3]    
    #politics_articles = published_articles.filter(section=Article.Section.POLITICS).order_by('-pub_date')[:3]
    tech_articles = published_articles.filter(section=Article.Section.TECHNOLOGY).order_by('-pub_date')[:3]
    #sports_articles = published_articles.filter(section=Article.Section.SPORTS).order_by('-pub_date')[:3]
    pop_culture_articles = published_articles.filter(section=Article.Section.POP_CULTURE).order_by('-pub_date')[:3]
    editorial_articles = published_articles.filter(section=Article.Section.EDITORIAL).order_by('-pub_date')[:3]
    recent_nonprioritized = published_articles.order_by('-pub_date').values_list('pk',flat=True)[:20]
    recent_articles = published_articles.filter(pk__in=list(recent_nonprioritized)).order_by('-priority')

    context = {
        'scitech_articles':scitech_articles,
        'pittsburgh_articles':pittsburgh_articles,
        #'politics_articles':politics_articles,
        'tech_articles':tech_articles,
        #'sports_articles':sports_articles,
        'pop_culture_articles':pop_culture_articles,
        'editorial_articles':editorial_articles,
        'recent_articles':recent_articles,
    }
    context.update(get_global_context())
    #print(str(context))
    return render(request,'home/index.html', context)

def scitech_section(request):
    articles = published_articles.filter(section=Article.Section.AT_SCITECH).order_by('-pub_date')[:20]
    #pittsburgh_articles = published_articles.filter(section=Article.Section.IN_PITTSBURGH).order_by('-pub_date')[:3]    
    #politics_articles = published_articles.filter(section=Article.Section.POLITICS).order_by('-pub_date')[:3]
    #tech_articles = published_articles.filter(section=Article.Section.TECHNOLOGY).order_by('-pub_date')[:3]
    #sports_articles = published_articles.filter(section=Article.Section.SPORTS).order_by('-pub_date')[:3]
    #pop_culture_articles = published_articles.filter(section=Article.Section.POP_CULTURE).order_by('-pub_date')[:3]
    #editorial_articles = published_articles.filter(section=Article.Section.EDITORIAL).order_by('-pub_date')[:3]
    #recent_nonprioritized = published_articles.order_by('-pub_date').values_list('pk',flat=True)[:20]
    #recent_articles = published_articles.filter(pk__in=list(recent_nonprioritized)).order_by('-priority')

    context = {
        'articles':articles,
        'section_name':"at scitech",
    }
    context.update(get_global_context())
    #print(str(context))
    return render(request,'home/section.html', context)

def pittsburgh_section(request):
    #scitech_articles = published_articles.filter(section=Article.Section.AT_SCITECH).order_by('-pub_date')[:3]
    articles = published_articles.filter(section=Article.Section.IN_PITTSBURGH).order_by('-pub_date')[:20]    
    #politics_articles = published_articles.filter(section=Article.Section.POLITICS).order_by('-pub_date')[:3]
    #tech_articles = published_articles.filter(section=Article.Section.TECHNOLOGY).order_by('-pub_date')[:3]
    #sports_articles = published_articles.filter(section=Article.Section.SPORTS).order_by('-pub_date')[:3]
    #pop_culture_articles = published_articles.filter(section=Article.Section.POP_CULTURE).order_by('-pub_date')[:3]
    #editorial_articles = published_articles.filter(section=Article.Section.EDITORIAL).order_by('-pub_date')[:3]
    #recent_nonprioritized = published_articles.order_by('-pub_date').values_list('pk',flat=True)[:20]
    #recent_articles = published_articles.filter(pk__in=list(recent_nonprioritized)).order_by('-priority')

    context = {
        'articles':articles,
        'section_name':"in pittsburgh",
    }
    context.update(get_global_context())
    #print(str(context))
    return render(request,'home/section.html', context)

def technology_section(request):
    #scitech_articles = published_articles.filter(section=Article.Section.AT_SCITECH).order_by('-pub_date')[:3]
    #pittsburgh_articles = published_articles.filter(section=Article.Section.IN_PITTSBURGH).order_by('-pub_date')[:3]    
    #politics_articles = published_articles.filter(section=Article.Section.POLITICS).order_by('-pub_date')[:3]
    articles = published_articles.filter(section=Article.Section.TECHNOLOGY).order_by('-pub_date')[:20]
    #sports_articles = published_articles.filter(section=Article.Section.SPORTS).order_by('-pub_date')[:3]
    #pop_culture_articles = published_articles.filter(section=Article.Section.POP_CULTURE).order_by('-pub_date')[:3]
    #editorial_articles = published_articles.filter(section=Article.Section.EDITORIAL).order_by('-pub_date')[:3]
    #recent_nonprioritized = published_articles.order_by('-pub_date').values_list('pk',flat=True)[:20]
    #recent_articles = published_articles.filter(pk__in=list(recent_nonprioritized)).order_by('-priority')

    context = {
        'articles':articles,
        'section_name':"technology",
    }
    context.update(get_global_context())
    #print(str(context))
    return render(request,'home/section.html', context)

def pop_culture_section(request):
    #scitech_articles = published_articles.filter(section=Article.Section.AT_SCITECH).order_by('-pub_date')[:3]
    #pittsburgh_articles = published_articles.filter(section=Article.Section.IN_PITTSBURGH).order_by('-pub_date')[:3]    
    #politics_articles = published_articles.filter(section=Article.Section.POLITICS).order_by('-pub_date')[:3]
    #tech_articles = published_articles.filter(section=Article.Section.TECHNOLOGY).order_by('-pub_date')[:3]
    #sports_articles = published_articles.filter(section=Article.Section.SPORTS).order_by('-pub_date')[:3]
    articles = published_articles.filter(section=Article.Section.POP_CULTURE).order_by('-pub_date')[:20]
    #editorial_articles = published_articles.filter(section=Article.Section.EDITORIAL).order_by('-pub_date')[:3]
    #recent_nonprioritized = published_articles.order_by('-pub_date').values_list('pk',flat=True)[:20]
    #recent_articles = published_articles.filter(pk__in=list(recent_nonprioritized)).order_by('-priority')

    context = {
        'articles':articles,
        'section_name':"pop culture",
    }
    context.update(get_global_context())
    #print(str(context))
    return render(request,'home/section.html', context)

def editorial_section(request):
    #scitech_articles = published_articles.filter(section=Article.Section.AT_SCITECH).order_by('-pub_date')[:3]
    #pittsburgh_articles = published_articles.filter(section=Article.Section.IN_PITTSBURGH).order_by('-pub_date')[:3]    
    #politics_articles = published_articles.filter(section=Article.Section.POLITICS).order_by('-pub_date')[:3]
    #tech_articles = published_articles.filter(section=Article.Section.TECHNOLOGY).order_by('-pub_date')[:3]
    #sports_articles = published_articles.filter(section=Article.Section.SPORTS).order_by('-pub_date')[:3]
    #pop_culture_articles = published_articles.filter(section=Article.Section.POP_CULTURE).order_by('-pub_date')[:3]
    articles = published_articles.filter(section=Article.Section.EDITORIAL).order_by('-pub_date')[:20]
    #recent_nonprioritized = published_articles.order_by('-pub_date').values_list('pk',flat=True)[:20]
    #recent_articles = published_articles.filter(pk__in=list(recent_nonprioritized)).order_by('-priority')

    context = {
        'articles':articles,
        'section_name':"editorial"
    }
    context.update(get_global_context())
    #print(str(context))
    return render(request,'home/section.html', context)

def generic(request):
    text_md = grab_md(request.resolver_match.view_name)

    context = {
        "text_md":text_md,
    }
    context.update(get_global_context())
    return render(request,'home/generic.html', context)

def aug2023_pdf(request):
    filepath = os.path.join('static','issues','aug2023.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
