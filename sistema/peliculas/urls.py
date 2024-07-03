from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('soporte/', views.soporte, name='soporte'),
    path('index/', views.index, name='index'),
    path('agregar/', views.agregar, name='agregar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('exit/', views.exit, name='exit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)