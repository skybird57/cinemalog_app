from django.test import TestCase
from users.models import CustomUser

class TestCustomUSer(TestCase):
    def setUp(self):
        print('setUp')
        user1=CustomUser.objects.create(phone='1111')
        user1.username="amir shiri"
        user1.save()
        

    def test_user_info(self):
        all=CustomUser.objects.all()
        self.assertEqual(all.count(),1)
        u1=CustomUser.objects.get(id=1)
        self.assertEqual(u1.username,"amir shiri")