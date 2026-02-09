from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote

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

class ListMedicalNotesView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de notas médicas asociadas a las citas.
    """
    allowed_methods = ['GET','POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar una nota médica específica utilizando su ID (pk).
    """
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()