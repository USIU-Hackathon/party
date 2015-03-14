# Create your views here.
from django.contrib.auth.models import User, Group


from rest_framework import viewsets
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from playlist.models import Playlist,Tracks
from playlist.serializers import UserSerializer, GroupSerializer, PlaylistSerializer,TracksSerializer
import soundcloud

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SoundCloudSearch(query):
	#create a client object with app credentials
	client = soundcloud.Client(client_id='ed485d39d5d8d1214fd3142ff2485c1b')
	
	#find all tracks from the Africas talking return message
	tracks = client.get('/tracks', q=query, license='cc-by-sa')

	""""
class DjGetMessageFromAfricasTalking():
	# Be sure to import the helper gateway class


    # Specify your login credentials
    username = 'hungai'
    apikey   = ''

    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)

# Any gateway errors will be captured by our custom Exception class below, 
# so wrap the call in a try-catch block
    try:
    # Our gateway will return 10 messages at a time back to you, starting with
    # what you currently believe is the lastReceivedId. Specify 0 for the first
    # time you access the gateway, and the ID of the last message we sent you
    # on subsequent results
        lastReceivedId = 0;
    
        while True:
	        messages = gateway.fetchMessages(lastReceivedId)
        
            for message in messages:
	            """print 'from=%s;to=%s;date=%s;text=%s;linkId=%s;' % (message['from'],
                                                                message['to'],
                                                                message['date'],
                                                                message['text'],
                                                                message['linKId'])"""
                query = (message['text'])
	            lastReceivedId = message['id']
        
            if len(messages) == 0:
	            break

            
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while fetching messages: %s' % str(e)
	
	SoundCloudSearch(query)
	"""
class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer

class TracksViewSet(viewsets.ModelViewSet):
	queryset =Tracks.objects.all()
	serializer_class = TracksSerializer
		



