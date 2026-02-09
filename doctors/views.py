from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailability, MedicalNote

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# GET /api/doctors => listar
# POST /api/doctors => crear  
# GET /api/doctors/<pk> => Detalle
# PUT /api/doctors/<pk> => Actualizar
# DELETE /api/doctors/<pk> => Eliminar

class ListDoctorsView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de doctores registrados en el sistema.
    """
    allowed_methods = ['GET','POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar un doctor específico utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ListDepartmentsView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de departamentos registrados en el sistema.
    """
    allowed_methods = ['GET','POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar un departamento específico utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de disponibilidades de los doctores registrados en el sistema.
    """
    allowed_methods = ['GET','POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar una disponibilidad específica utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer

class ListMedicalNoteView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de notas médicas registradas en el sistema.
    """
    allowed_methods = ['GET','POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar una nota médica específica utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer