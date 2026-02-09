from django.urls import path
from .views import ListAppointmentsView, DetailAppointmentView

urlpatterns = [
    path('appointments/', ListAppointmentsView.as_view()),
    path('appointments/<int:pk>/', DetailAppointmentView.as_view()),
]