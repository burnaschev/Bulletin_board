from rest_framework.fields import DateTimeField
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from bulletin.models import Ad, Feedback
from users.models import User


class AdsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email='Dilor1900@gmail.com',
            password="qwerty123qwerty2",
            first_name='Artur',
            last_name="Bu",
            phone="892321231"
        )
        self.client.force_authenticate(user=self.user)
        self.iso_date_field = DateTimeField()

        self.ads = Ad.objects.create(
            title="test",
            author=self.user,
            description="new ads"
        )

    def test_get_ads_list(self):
        """ Test for getting list fo ads """

        response = self.client.get(
            reverse('bulletin:ad-list')
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.ads.id,
                        "title": self.ads.title,
                        "price": self.ads.price,
                        "description": self.ads.description,
                        "created_at": self.iso_date_field.to_representation(self.ads.created_at),
                        "author": self.ads.author_id
                    }
                ]
            }
        )

    def test_ads_create(self):
        """ Test for create ads """

        data = {
            "title": "test2",
            "description": 'new ads 2'
        }

        response = self.client.post(
            reverse('bulletin:ad-create'),
            data=data
        )
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)

        self.assertEquals(Ad.objects.all().count(),
                          2
                          )

    def test_update_ads(self):
        """ Test for update ads """

        data = {
            'title': 'update test',
            "description": 'update new ads 2'
        }

        response = self.client.put(
            reverse('bulletin:ad-update', args=[self.ads.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_ads(self):
        """ Test for delete ads """

        response = self.client.delete(reverse('bulletin:ad-delete', args=[self.ads.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FeedbackTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email='artur_321@gmail.com',
            password="qwerty123qwerty2",
            first_name='Artur',
            last_name="Bu",
            phone="892321231"
        )

        self.client.force_authenticate(user=self.user)
        self.iso_date_field = DateTimeField()

        self.ads = Ad.objects.create(
            title="test3",
            author=self.user,
            description="new ads3"
        )

        self.feedback = Feedback.objects.create(
            text="test",
            ad=self.ads,
            author=self.user
        )

    def test_get_feedback_list(self):
        """ Test for getting list fo feedback """

        response = self.client.get(
            reverse('bulletin:feedback-list')
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            [
                {
                    "id": self.feedback.id,
                    "text": self.feedback.text,
                    "created_at": self.iso_date_field.to_representation(self.feedback.created_at),
                    "author": self.feedback.author_id,
                    "ad": self.feedback.ad_id
                }
            ]
        )

    def test_create_feedback(self):
        """ Test for create feedback """

        data = {
            "ad": self.ads.id,
            "author": self.user.id,
            "text": self.feedback.text
        }

        response = self.client.post(
            reverse('bulletin:feedback-list'),
            data=data
        )
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)

        self.assertEquals(Feedback.objects.all().count(),
                          2
                          )

    def test_update_feedback(self):
        """ Test for update feedback """

        data = {
            'text': 'update test',
            "author": self.feedback.author_id,
            "ad": self.feedback.ad_id
        }

        response = self.client.put(
            reverse('bulletin:feedback-detail', args=[self.feedback.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_feedback(self):
        """ Test for delete feedback """

        response = self.client.delete(reverse('bulletin:feedback-detail', args=[self.feedback.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
