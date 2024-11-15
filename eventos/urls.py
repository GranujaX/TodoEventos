"""PP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eventos import views as eventoVista
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet

router = DefaultRouter()
router.register(r'eventosAPI', EventoViewSet)


urlpatterns = [
    path('', eventoVista.home, name='home'),
    path('<int:year>/<str:month>/', eventoVista.home),
    path('eventos', eventoVista.all_events, name="eventlist"),
    path('add_venue',eventoVista.add_venue, name='add_venue'),
    path('venue',eventoVista.venues, name='venue'),
    path('show_venue/<venue_id>',eventoVista.show_venues, name='show_venue'),
    path('show_event/<event_id>',eventoVista.show_events, name='show_event'),
    path('search_result',eventoVista.search_result, name='search_result'),
    path('update_venue/<venue_id>', eventoVista.update_venue, name='update_venue'),
    path('add_event',eventoVista.add_event, name='add_event'),
    path('update_event/<event_id>',eventoVista.update_event, name='update_event'),
    path('delete_event/<event_id>',eventoVista.delete_event, name='delete_event'),
    path('delete_venue/<venue_id>',eventoVista.delete_venue, name='delete_venue'),
    #path('map/', eventoVista.show_map, name='show_map'),
    path('map/<int:venue_id>/', eventoVista.show_map, name='show_map'),
    path('', include(router.urls)),
    path('download_pdf_report',eventoVista.download_pdf_report, name='download_pdf_report'),
    path('download_excel_report',eventoVista.download_excel_report, name='download_excel_report'),
 
    
   
    
    #debug funciona
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
