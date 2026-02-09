from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__' # esto es para incluir todos los campos del modelo Doctor, puedes especificar campos específicos si lo deseas
    
    def validate_email(self, value):
        if "@example.com" in value:
            return value
        raise serializers.ValidationError("El correo electrónico debe ser del dominio @example.com")
    
    def validate(self, attrs):
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation'] == True:
            raise serializers.ValidationError(
                "Por favor, ingrese un número de contacto válido antes de irte a vacaciones"
            )
        return super().validate(attrs)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'