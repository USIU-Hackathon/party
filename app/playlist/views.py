# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from playlist.serializers import UserSerializer, GroupSerializer, PlaylistSerializer

class UserViewSet(viewsets.ModelViewSet)

"""
API endpoint that allows users to be viewed or date
"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

"""
API endpoint that allows users to be viewed or date
"""

class GroupViewSet(viewsets.ModelViewSet):
		queryset = Group.objects.all()
		serializer_class = GroupSerializer

"""
API endpoint that allows playlist to be viewed 
"""

class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


