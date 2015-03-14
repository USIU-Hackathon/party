__author__ = 'Nelly'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from  playlist.models import Playlist,Tracks,AfricasTalking



class AfricaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AfricasTalking
		fields = ('number_from','to','text','linkId','date','id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','email')


class GroupSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
                model = Group
                fields = ('url', 'name')

class PlaylistSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		        model = Playlist
		        fields = ('name','user','created_at','updated_at')

class TracksSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		        model = Tracks
		        fields =('name','artist','playlist','stream_url')
			