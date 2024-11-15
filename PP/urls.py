from django.contrib import admin
from django.urls import path, include
from eventos import views as eventoVista
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eventos.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls')),
    #path("%%")
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
