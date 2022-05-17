from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class HotelCreateAPIViewTestCase(APITestCase):
    url = reverse("hotel:hotel_list")

    def setUp(self):
        self.user = User.objects.create_user(username='user')
        self.user.set_password('123456')
        self.user.save()
        self.client.login(username='user', password='123456')

    def test_create_hotel(self):
        response = self.client.post(self.url, {"name": "razi",
                                               "location": "tehran",
                                               "phone": '09111112345'})
        self.assertEqual(201, response.status_code)