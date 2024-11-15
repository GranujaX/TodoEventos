from django.contrib import admin
from .models import Venue
from .models import User
from .models import Event


admin.site.register(User)




#crea el registro Venue y lo customiza
@admin.register(Venue)
class VenueADmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    ordering = ('name',)
    search_fields = ('name', 'address')

#crea el registro Event y lo customiza
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'), 'event_date', 'company')
    list_display = ('name','event_date')
    list_filter = ('venue', 'event_date' )
    ordering = ('event_date',)