from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UsersTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_user_register(self):
        """ Test created user """

        data = {
            "email": 'Dilor1900@gmail.com',
            "password": "qwerty123qwerty2",
            "first_name": 'Artur',
            "last_name": "Bu",
            "phone": 892321231
        }

        response = self.client.post(
            reverse('users:users-list'),
            data=data
        )
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)
        self.assertEquals(User.objects.all().count(),
                          1
                          )
