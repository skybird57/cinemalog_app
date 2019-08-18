from rest_framework.test import APITestCase,RequestsClient
from django.urls import reverse
from rest_framework import status
from users.models import CustomUser,CustomUserToken

class UserTestAPI(APITestCase):
    def setUp(self):
        user1=CustomUser.objects.create(phone='09121112233')
        user1.username='amir shiri'
        user1.save()
        token=CustomUserToken.objects.create(user_id=1,deviceId='sample',deviceType=1,validToken='sample',token='sample')
    def test_post_getphone(self):
        url=reverse('get phone')
        data={'phone':'09303331122'}
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(),2)
        self.assertEqual(CustomUser.objects.get(phone='09303331122').username,None)

    def test_post_signup(self):
        url=reverse('sign up')
        data={'phone':'09121112233',
            'deviceId':'sample',
            'validToken':'sample',
            'deviceType':'1'}
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,200)
        print(CustomUserToken.objects.get(user_id=1).token)

    def test_put_updateprofile(self):
        self.client=RequestsClient()
        url=reverse('update profile')
        data={'username':'amir amir','phone':'09121112233'}
        headers={"userId":"1","token":"sample"}
        response=self.client.put('http://localhost:8000/user/api/updateprofile',data=data,headers=headers)
        self.assertEqual(response.status_code,204)
        self.assertEqual(CustomUser.objects.get(pk=1).username,'amir amir')
        t=CustomUserToken.objects.get(user_id=1)
        self.assertEqual(t.token,'sample')


    def test_put_setNotify(self):
        self.client=RequestsClient()
        url=reverse('set notify')
        data={'notification_status':'true','phone':'09121112233'}
        headers={'userId':'1','token':'sample'}
        self.client.head=headers
        response=self.client.put('http://localhost:8000/user/api/setNotificationStatus',data,headers=headers)
        self.assertEqual(CustomUser.objects.get(pk=1).notification_status,True)
