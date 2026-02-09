from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# GET /api/patients => listar
# POST /api/patients => crear  
# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Actualizar
# DELETE /api/patients/<pk> => Eliminar

class ListPatientsView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de pacientes registrados en el sistema.
    """
    allowed_methods = ['GET','POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar un paciente específico utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class ListInsurancesView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de seguros asociados a un paciente específico.
    """

    allowed_methods = ['GET','POST']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar un seguro específico utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

class ListMedicalRecordsView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de registros médicos asociados a un paciente específico.
    """
    allowed_methods = ['GET','POST']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()

class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar un registro médico específico utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()