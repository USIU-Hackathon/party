from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def song_count(self):
        return self.song_set.count()
    
    def __unicode__(self):
        return u'%s - %s' %(self.user, self.name)
    
class Tracks(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist)
    stream_url = models.CharField(max_length=200)
    
    
    def __unicode__(self):
        return u'%s' %(self.name)