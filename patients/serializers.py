from datetime import date
from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer

class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointments',
        ]
    def validate_email(self, value):
        if "@example.com" in value:
            return value
        raise serializers.ValidationError("El correo electrónico debe ser del dominio @example.com")
    
    def validate(self, attrs):
        if len(attrs['contact_number']) < 10:
            raise serializers.ValidationError(
                "Por favor, ingrese un número de contacto válido"
            )
        return super().validate(attrs)
    
    def validate_birth_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser en el futuro")
        return value

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__' 

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__' 