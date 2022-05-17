from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from articles import views as article_views

from django.views.static import serve
# from django.conf.urls import url

# from django.shortcuts import urls
from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('articles/',include('articles.urls')),
    path('about/',views.about),
    path('',article_views.article_list, name='home'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
