from .serializers import DoctorSerializer
from .models import Doctor

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