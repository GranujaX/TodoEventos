from rest_framework import serializers
from .models import Event

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Esto incluirá todos los campos del modelo
