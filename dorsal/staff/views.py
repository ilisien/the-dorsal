from django.shortcuts import render
from staff.models import Profile
from articles.models import published_articles
import datetime
from globals import get_global_context

def staff(request, first_name, last_name):
    staff_member = Profile.objects.get(user__first_name__icontains=first_name,user__last_name__icontains=last_name)
    author_articles = published_articles.filter(author=staff_member).order_by('-pub_date')[:5]

    context = {
        "staff_member":staff_member,
        "author_articles":author_articles
    }

    context.update(get_global_context())

    return render(request,'staff/staff.html', context)