"""Fakegram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings # esto es para poder ver las imágenes en el panel en desarrollo
from django.conf.urls.static import static # esto es para poder ver las imágenes en el panel en desarrollo
from django.urls import path

# Local views
from fakegram import views as local_views

# Posts views
from posts import views as posts_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world), 
    path('hi/<str:name>/<int:age>/', local_views.hi),

    path('posts', posts_views.list_posts)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # esto es para poder ver las imágenes en el panel en desarrollo
