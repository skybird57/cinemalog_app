from rest_framework.test import APITestCase
from users.models import CustomUser

class UserTestAPI(APITestCase):
    def setUp(self):
        user1=CustomUser.objects.create(phone='09121112233')
        user1.username='amir shiri'
        user1.save()
    def test_get_method(self):
        url='http://localhost:8000/user/api/getphone?phone=09121112233'
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        #u=CustomUser.objects.filter(username='amir shiri')

    def test_post_method_success(self):
        url='http://localhost:8000/user/api/getphone?phone=09123332233'
        response=self.client.post(url)
        self.assertEqual(response.status_code,201)

    def test_post_method_fail(self):
        url='http://localhost:8000/user/api/getphone?phone=08121112233'
        response=self.client.post(url)
        self.assertEqual(response.status_code,404)
