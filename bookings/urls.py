from django.urls import path
from .views import ListAppointmentsView, DetailAppointmentView, ListMedicalNotesView, DetailMedicalNoteView
from rest_framework.routers import DefaultRouter
from bookings.viewsets import AppointmentViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical-notes', MedicalNoteViewSet)

urlpatterns = [
    path('appointments/', ListAppointmentsView.as_view()),
    path('appointments/<int:pk>/', DetailAppointmentView.as_view()),
    path('medical-notes/', ListMedicalNotesView.as_view()),
    path('medical-notes/<int:pk>/', DetailMedicalNoteView.as_view())
] + router.urls