from django.urls import include, path, re_path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
]