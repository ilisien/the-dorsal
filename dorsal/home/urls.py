from django.urls import include, path, re_path
from home import views

urlpatterns = [
    path('',views.index),
    path('contact/',views.contacts),
    path('about/',views.about)
]