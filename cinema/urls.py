from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main, name='main'),
    path('films/', main_views.films, name='films'),
    path('film/<int:film_id>', main_views.film, name='film'),
    path('news_post/<int:post_id>', main_views.news_post, name='news_post'),
    path('news/', main_views.news, name='news'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
