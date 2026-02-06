from .serializers import DoctorSerializer
from .models import Doctor

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# GET /api/doctors => listar
# POST /api/doctors => crear  
# GET /api/doctors/<pk> => Detalle
# PUT /api/doctors/<pk> => Actualizar
# DELETE /api/doctors/<pk> => Eliminar

@api_view(['GET', 'POST'])
def list_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def detail_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    if request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
