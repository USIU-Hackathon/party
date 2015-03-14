# Create your views here.
from django.contrib.auth.models import User, Group


from rest_framework import viewsets

from playlist.models import Playlist,Tracks,AfricasTalking
from playlist.serializers import UserSerializer, GroupSerializer, PlaylistSerializer,TracksSerializer, AfricaSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer

class TracksViewSet(viewsets.ModelViewSet):
	queryset =Tracks.objects.all()
	serializer_class = TracksSerializer




class AfricaViewSet(viewsets.ModelViewSet):
	queryset = AfricasTalking.objects.all()
	serializer_class = AfricaSerializer
		

		



