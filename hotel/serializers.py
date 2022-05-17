from rest_framework import serializers
from .models import Hotel, Room, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'location', 'phone']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['number', 'capacity', 'hotel']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['date', 'room']


class RoomSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['number', 'capacity', 'hotel']


class ReserveSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['user', 'room', 'date']
