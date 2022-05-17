from django_filters.rest_framework import DjangoFilterBackend
from .models import Hotel, Room, Reservation
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import HotelSerializer, ReservationSerializer, RoomSerializer


# Create your views here.
class HotelListView(generics.ListCreateAPIView):
    model = Hotel
    '''Check in a user Logged or no?, returns the User logged'''
    serializer_class = HotelSerializer
    '''Import Serializer Reserve for Show ApiView '''
    permission_classes = [IsAuthenticated]
    '''Queryset for GET The objects from Hotel table '''
    queryset = Hotel.objects.all()
    '''Option : Search in records in this Table'''
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']
    ''' THIS LINE check the user can watch and create record  '''
    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class RoomListCreateView(generics.ListCreateAPIView):

    template_name = 'index_list.html'

    model = Room
    '''Check in a user Logged or no?, returns the User logged'''
    serializer_class = RoomSerializer
    '''Import Serializer Reserve for Show ApiView '''
    permission_classes = [IsAuthenticated]
    ''' GET The objects from Room table '''
    queryset = Room.objects.all()
    '''Option : Search in records in this Table'''
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['capacity', 'hotel']


class ReserveListCreate(generics.ListCreateAPIView):
    model = Reservation
    '''Check in a user Logged or no?, returns the User logged'''
    permission_classes = [IsAuthenticated]
    '''Import Serializer Reserve for Show ApiView '''
    serializer_class = ReservationSerializer
    ''' GET The objects from Reservation table '''
    queryset = Reservation.objects.all()
    '''Option : Search in records in this Table'''
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['room', 'date']
    ''' THIS LINE check the user can watch and create record  '''
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
