from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main, name='main')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
