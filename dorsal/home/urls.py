from django.urls import include, path, re_path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('contact/',views.generic,name='contact'),
    path('about/',views.generic,name='about'),
    path('open-source/',views.generic,name='open-source'),
    path('advertise/',views.generic,name='advertise'),
    path('apply/',views.generic,name='apply'),
    #path('write/',views.generic,name='write'),
    path('physical-newspaper/',views.generic,name='physical-newspaper'),
    #path('subscribe/',views.generic,name='subscribe'),
    path('fonts/',views.generic,name='fonts'),

]