from rest_framework import generics


from todos import models
from .serializers import TodoSerializer, UserSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class=UserSerializer
    
