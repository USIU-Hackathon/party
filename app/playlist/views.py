# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from playlist.serializers import UserSerializer, GroupSerializer, PlaylistSerializer,TracksSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer



class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class TracksViewSet(viewsets.ModelViewSet):
	queryset =Group.objects.all()
	serializer_class = GroupSerializer
		



