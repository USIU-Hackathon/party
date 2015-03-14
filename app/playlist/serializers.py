__author__ = 'Nelly'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from  playlist.models import Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username''email', 'group')


class GroupSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
                model = Group
                fields = ('url', 'name')

class PlaylistSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		        model = Playlist
		        fields = ('name','user','created_at','updated_at')
