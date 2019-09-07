"""Fakegram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings # esto es para poder ver las imágenes en el panel en desarrollo
from django.conf.urls.static import static # esto es para poder ver las imágenes en el panel en desarrollo
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
  
    path('users/', include(('users.urls', 'users'), namespace='users')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # esto es para poder ver las imágenes en el panel en desarrollo
