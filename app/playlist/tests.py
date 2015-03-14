import time
from playlist.models import Playlist, Tracks

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from datetime import datetime


class PlayListTest(TestCase):
    def test_saving_retrieving_playlist(self):
        playlist = Playlist()
        playlist.name = "First ever playlist"
        #playlist.user = User
        playlist.created_at = datetime.now()
        time = datetime.now()
        playlist.save()
        
        playlist_ = Playlist.objects.all()
        
        firstplaylist = playlist_[0]
        
        self.assertEqual(firstplaylist.name, "First ever playlist")
        #self.assertEqual(firstplaylist.created_at, time)
        
    