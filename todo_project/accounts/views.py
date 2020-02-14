from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,authentication_classes,permission_classes


from .models import UserProfile
from .permissions import IsOwnerProfileReadOnly
from .serializers import UserProfileSerializer


# Create your views here.
class UserProfileCreateView(ListCreateAPIView):
    queryset = UserProfile
    serializer_class=UserProfileSerializer
    permission_classes=(IsAuthenticated)
    authentication_classes=(TokenAuthentication)
    http_method_names = ['get', 'head']


    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes=[IsOwnerProfileReadOnly, IsAuthenticated]