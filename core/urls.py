from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),
    path('', include('clientes.urls')),
    path('', include('funcionarios.urls')),
    path('', include('plataforma.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
