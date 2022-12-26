from django.urls import include, path, re_path
from articles import views
from home.views import redirect_to_home

urlpatterns = [
    path("",redirect_to_home),
    path("<int:article_id>/",views.article),
    path("<int:year>/<int:month>/<int:day>/<str:article_title>/",views.article)
]