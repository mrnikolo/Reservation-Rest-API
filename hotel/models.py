from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    manager = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    capacity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=False, blank=False)
    date = models.DateField(null=False, blank=False)

    class Meta:
        unique_together = [
            'room', 'date'
        ]
