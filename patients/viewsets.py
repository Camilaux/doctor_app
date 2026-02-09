from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import InsuranceSerializer, MedicalRecordSerializer, PatientSerializer
from .models import Patient, Insurance, MedicalRecord

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(['GET'], detail=True, url_path='medical-records')
    def get_medical_records(self, request, pk):
        patient = self.get_object()
        medical_records = patient.medical_history.all()
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)

class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer