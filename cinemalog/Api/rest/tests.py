from rest_framework.test import APITestCase,RequestsClient
from rest_framework import status
from django.urls import reverse
from cinemalog.models import ApplicationVersion
from datetime import datetime

class CinemalogTest(APITestCase):
    def setUp(self):
        ApplicationVersion.objects.create(platform=1,required_version=3.2,
                last_version=3.6,generated_at=datetime.today(),user_id=1)
    def test_appversion(self):
        url=reverse('rest force update')
        params={'version':'3','platform':'1'}