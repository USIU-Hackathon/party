# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from playlist.models import Playlist,Tracks
from playlist.serializers import UserSerializer, GroupSerializer, PlaylistSerializer,TracksSerializer
import soundcloud

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class SoundCloudSearch():
	#create a client object with app credentials
	client = soundcloud.Client(client_id='ed485d39d5d8d1214fd3142ff2485c1b')
	
	#find all tracks from the Africas talking return message
	tracks = client.get('/tracks', q={{to finish}}, license=)
	
class DjGetMessageFromAfricasTalking():
	
	
	
	
		




class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer

class TracksViewSet(viewsets.ModelViewSet):
	queryset =Tracks.objects.all()
	serializer_class = TracksSerializer
		



