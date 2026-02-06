from django.urls import path
from .views import detail_patient, list_patients

urlpatterns = [
    path('patients', list_patients),
    path('patients/<int:pk>/', detail_patient)
]