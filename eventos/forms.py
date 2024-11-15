from django import forms
from django.forms import ModelForm
from .models import Venue, Event


#create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','phone','email_address')
        #create styles
        widgets = {'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del lugar'}),
                  'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
                  'phone':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numero de contacto'}),
                  'email_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electronico'})
                  }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','venue','company','description')
        #create styles

        widgets = {'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del evento'}),
                  'event_date':forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'Fecha del evento'}),
                  'venue':forms.Select(attrs={'class':'form-select', 'placeholder':'Lugar del evento'}),
                  'company':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Compañia organizadora'}),
                  'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion del evento'})
                  }
        

