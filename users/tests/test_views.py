from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from users.models import User



class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.list_url = reverse('list_user')
        self.create_url = reverse('user')

    def test_list_users(self):

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_create_users(self):

        response = self.client.post(
            self.create_url,
            {
              "city" : "Puerto Caldas",
              "email" :  "coink2@coink.com",
              "first_name" : "Andrea",
              "last_name" : "Mora"  
            }
            )
        self.assertEqual(response.status_code, 200)

    