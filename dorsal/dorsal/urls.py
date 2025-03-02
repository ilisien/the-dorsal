from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
import os.path

from django.http import Http404
from django.http import HttpResponseServerError
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.core.exceptions import SuspiciousOperation

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from home import urls as home_urls
from home.views import redirect_to_home

from articles import urls as article_urls
from staff import urls as staff_urls
from globals.views import see404

handler404 = 'globals.views.error404'
handler500 = 'globals.views.error500'
handler403 = 'globals.views.error403'
handler400 = 'globals.views.error400'


def fake_404(request):
    raise Http404

def fake_500(request):
    raise Exception("oops!")

def fake_403(request):
    return HttpResponseForbidden()

def fake_400(request):
    raise SuspiciousOperation

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('debug_404/',see404),
    path('404/',fake_404),
    path('500/',fake_500),
    path('403/',fake_403),
    path('400/',fake_400),

    path("",redirect_to_home),
    path("home/",include(home_urls),name='home'),
    path("article/",include(article_urls),name='articles'),
    path("staff/",include(staff_urls),name='staffs'),
    path("sections/",include(home_urls),name='sections')
]


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
]