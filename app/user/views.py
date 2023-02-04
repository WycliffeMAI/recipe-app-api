"""
Views for the user API
"""
from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create as new user in the system."""
    serializer_class = UserSerializer

