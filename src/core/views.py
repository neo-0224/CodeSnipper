from django.contrib.auth.models import User, Group
from rest_framework.generics import ListAPIView
from . import serializers

# Create your views here.

class UserView(ListAPIView):
    """
    Viewset showing the user to be viewed and to be edited.
    """
    # queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class GroupView(ListAPIView):
    """
    Viewset showing the user groups to be viewed and to be edited.
    """
    # queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

