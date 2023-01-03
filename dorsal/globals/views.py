from django.shortcuts import render
from django.http import HttpResponse
from globals import get_global_context

def error404(request, exception):
    error_code = "404"
    what_happened = "What you are looking for could not be found. If you reached this page by clicking on a link, please come back soon; this site is still under development!"
    context = {
        'error_code':error_code,
        'what_happened':what_happened
    }
    context.update(get_global_context())

    return render(request,'globals/error.html', context)

def error500(request):
    error_code = "500"
    what_happened = "There is a server problem! We're working hard to get it working again!"
    context = {
        'error_code':error_code,
        'what_happened':what_happened
    }
    context.update(get_global_context())

    return render(request,'globals/error.html', context)

def error403(request, exception):
    error_code = "403"
    what_happened = "You do not have permission to access this page, perhaps you need to log in as a staff member?"
    context = {
        'error_code':error_code,
        'what_happened':what_happened
    }
    context.update(get_global_context())

    return render(request,'globals/error.html', context)

def error400(request, exception):
    error_code = "400"
    what_happened = "This link does not seem to work."
    context = {
        'error_code':error_code,
        'what_happened':what_happened
    }
    context.update(get_global_context())

    return render(request,'globals/error.html', context)

def see404(request):
    error_code = "404"
    what_happened = "What you are looking for could not be found. If you reached this page by clicking on a link, please come back soon; this site is still under development!"
    context = {
        'error_code':error_code,
        'what_happened':what_happened
    }
    context.update(get_global_context())

    return render(request,'globals/error.html', context)