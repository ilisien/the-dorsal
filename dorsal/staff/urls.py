from django.urls import include, path, re_path
from staff import views
from home.views import redirect_to_home

urlpatterns = [
    path("<str:first_name>_<str:last_name>/",views.staff,name="staff"),
]