from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .permissions import IsOwnerProfileReadOnly
from .serializers import UserProfileSerializer

# Create your views here.
class UserProfileCreateView(ListCreateAPIView):
    queryset = UserProfile
    serializer_class=UserProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes=[IsOwnerProfileReadOnly, IsAuthenticated]