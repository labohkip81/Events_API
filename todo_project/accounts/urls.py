from django.urls import path
from .views import UserProfileCreateView, UserProfileDetailView

urlpatterns = [
     #gets all user profiles and create a new profile
    path("all-profiles",UserProfileCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",UserProfileDetailView.as_view(),name="profile"),
]