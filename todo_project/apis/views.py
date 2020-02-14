from rest_framework import generics


from todos import models
from Events.models import EventsDetails
from .serializers import TodoSerializer,EventSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


#Event details views for api's

class ListEvents(generics.ListCreateAPIView):
    queryset = EventsDetails.objects.all()
    serializer_class = EventSerializer

class DetailEvents(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventsDetails.objects.all()
    serializer_class = EventSerializer