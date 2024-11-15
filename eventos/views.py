from django.shortcuts import render, redirect
from django.http import HttpResponse
import calendar 
from calendar import HTMLCalendar 
from datetime import datetime  
from .models import Event, Venue, User
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render
import requests
from .serializers import EventoSerializer
from rest_framework import viewsets
from .report_generators import PDFReportGenerator, ExcelReportGenerator
from django.http import FileResponse
from .utils import get_data_from_api
from .dummy import create_dummy

# Create your views here.

def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
    #Change month format 
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    #Create calendar
    calendario = HTMLCalendar().formatmonth(year, month_number)
    #Get curretn year
    now = datetime.now()
    current_year = now.year

    return render(request, 'eventos/home.html', {"calendario":calendario, "current_year":current_year})



def prendas(request):
    respuesta = get_data_from_api(request)
    for item in respuesta:
        print(item)
    return render(request,'eventos/prendas.html',{'respuesta':respuesta})
     

#muestra todos los eventos
def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'eventos/eventlist.html', {'event_list':event_list})

#muestra y hace la logica de la seccion addvenue que añade un lugar
def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if'submitted' in request.GET:
            submitted = True

    form = VenueForm
    return render(request, 'eventos/add_venue.html', {'form':form, 'submitted':submitted})


def venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'eventos/venue.html', {'venue_list':venue_list})


def show_venues(request, venue_id):
    #venue_list = Venue.objects.all()
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'eventos/show_venue.html', {'venue':venue})

def show_events(request, event_id):
    #venue_list = Venue.objects.all()
    event = Event.objects.get(pk=event_id)
    return render(request, 'eventos/show_event.html', {'event':event})

def search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venue_results = Venue.objects.filter(name__icontains=searched)
        event_results = Event.objects.filter(name__icontains=searched)
        user_results = User.objects.filter(username__icontains=searched)

        # Combina los resultados en una lista de tuplas (resultado, tipo)
        results = [(result, 'Venue') for result in venue_results] + [(result, 'Event') for result in event_results] + [(result, 'User') for result in user_results]

        return render(request, 'eventos/search_result.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'eventos/search_result.html', {})

def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('venue')

	return render(request, 'eventos/update_venue.html', 
		{'venue': venue,
		'form':form})


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if'submitted' in request.GET:
            submitted = True

    form = EventForm
    return render(request, 'eventos/add_event.html', {'form':form, 'submitted':submitted})

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if form.is_valid():
	    form.save()
	    return redirect('eventlist')

    return render(request, 'eventos/update_event.html', 
	    {'event': event,
	    'form':form})

#Eliminar C.R.U.D
def delete_event(request, event_id):
     event = Event.objects.get(pk=event_id)
     event.delete()
     return redirect('eventlist')

def delete_venue(request, venue_id):
     venue = Venue.objects.get(pk=venue_id)
     venue.delete()
     return redirect('venue')


#def show_map(request):
#    return render(request, 'eventos/map.html', {'api_key': 'AIzaSyDDmNlCxUaPrnv-pgCY_gYEKApbu7A1sm8'})


def show_map(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'eventos/map.html', {'api_key': 'AIzaSyDDmNlCxUaPrnv-pgCY_gYEKApbu7A1sm8', 'direccion': venue.address})


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventoSerializer


def download_pdf_report(request):
    events = Event.objects.all()  # Obtén todos los eventos
    generator = PDFReportGenerator()
    generator.generate(events)

    response = FileResponse(open('events_report.pdf', 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="events_report.pdf"'
    return response

def download_excel_report(request):
    events = Event.objects.all()  # Obtén todos los eventos
    generator = ExcelReportGenerator()
    generator.generate(events)

    response = FileResponse(open('events_report.xlsx', 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="events_report.xlsx"'
    return response