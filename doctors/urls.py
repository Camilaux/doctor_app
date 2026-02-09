from django.urls import path
from .views import (
    ListDoctorsView, 
    DetailDoctorView,
    ListDepartmentsView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailMedicalNoteView
    )
from rest_framework.routers import DefaultRouter
from .viewsets import DepartmentViewSet, DoctorAvailabilityViewSet, DoctorViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('doctor_availabilities', DoctorAvailabilityViewSet)
router.register('medical_notes', MedicalNoteViewSet)


urlpatterns = [
    path('doctors', ListDoctorsView.as_view()),
    path('doctors/<int:pk>', DetailDoctorView.as_view()),
    path('departments', ListDepartmentsView.as_view()),
    path('departments/<int:pk>', DetailDepartmentView.as_view()),
    path('doctor_availabilities', ListDoctorAvailabilityView.as_view()),
    path('doctor_availabilities/<int:pk>', DetailDoctorAvailabilityView.as_view()),
    path('medical_notes', ListMedicalNoteView.as_view()),
    path('medical_notes/<int:pk>', DetailMedicalNoteView.as_view())
] + router.urls