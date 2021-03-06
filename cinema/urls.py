from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', main_views.main, name='main'),
    path('logout/', main_views.logout_redirect, name='logout'),
    path('films/', main_views.films, name='films'),
    path('film/<int:film_id>', main_views.film, name='film'),
    path('news_post/<int:post_id>', main_views.news_post, name='news_post'),
    path('news/', main_views.news, name='news'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
