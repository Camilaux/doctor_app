from .serializers import AppointmentSerializer
from .models import Appointment

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# GET /api/appointments/ => listar
# POST /api/appointments/ => crear  
# GET /api/appointments/<pk>/ => Detalle
# PUT /api/appointments/<pk>/ => Actualizar
# DELETE /api/appointments/<pk>/ => Eliminar

class ListAppointmentsView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de citas médicas programadas
    """
    allowed_methods = ['GET','POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar una cita médica específica utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()