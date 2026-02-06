from rest_framework import serializers
from .models import Appointment, MedicalNote

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__' # esto es para incluir todos los campos del modelo Appointment, puedes especificar campos específicos si lo deseas

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__' 
        