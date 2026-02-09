from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsDoctor
from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment

from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsDoctor]
    
    @action(['post'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({'status': 'El doctor está de vacaciones'})
    
    @action(['post'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({'status': 'El doctor ya no está de vacaciones'})
    
    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()
        
        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)

    @action(['DELETE'], detail=True, url_path=r'appointments/(?P<appointment_id>\d+)/delete')
    def delete_appointment(self, request, pk, appointment_id=None):
        doctor = self.get_object()
        appointment = get_object_or_404(Appointment, pk=appointment_id, doctor=doctor)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer

class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer