from django.urls import include, path, re_path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('contact/',views.generic,name='contact'),
    path('about/',views.generic,name='about'),
    path('open-source/',views.generic,name='open-source'),
    path('advertise/',views.generic,name='advertise'),
    path('apply/',views.generic,name='apply'),
    path('physical-newspaper/',views.generic,name='physical-newspaper'),
    path('fonts/',views.generic,name='fonts'),
    path('scitech/',views.scitech_section,name='at-scitech'),
    path('pittsburgh/',views.pittsburgh_section,name='in-pittsburgh'),
    path('tech/',views.technology_section,name='technology'),
    path('pop/',views.pop_culture_section,name='pop-culture'),
    path('editorials/',views.editorial_section,name='editorial'),
]