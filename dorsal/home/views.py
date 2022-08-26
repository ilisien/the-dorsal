from django.shortcuts import render
from django.shortcuts import redirect

def redirect_to_home(request):
    return redirect('home/')

def index(request):
    pass

def contact(request):
    pass

def about(request):
    pass