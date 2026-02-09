from datetime import date
from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'  # esto es para incluir todos los campos del modelo Patient, puedes especificar campos específicos si lo deseas
    
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