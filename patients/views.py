from .serializers import PatientSerializer
from .models import Patient

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