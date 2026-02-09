from django.urls import path
from .views import (
    ListPatientsView, 
    DetailPatientView, 
    ListInsurancesView, 
    DetailInsuranceView, 
    ListMedicalRecordsView, 
    DetailMedicalRecordView
)
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('insurances', InsuranceViewSet)
router.register('medical-records', MedicalRecordViewSet) 

urlpatterns = [
    path('patients', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
    path('insurances', ListInsurancesView.as_view()),
    path('insurances/<int:pk>/', DetailInsuranceView.as_view()),
    path('medical-records', ListMedicalRecordsView.as_view()),
    path('medical-records/<int:pk>/', DetailMedicalRecordView.as_view())
] + router.urls