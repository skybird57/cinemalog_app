from rest_framework.test import APITestCase,RequestsClient
from django.urls import reverse
from rest_framework import status
from users.models import CustomUser,CustomUserToken

class UserTestAPI(APITestCase):
    def setUp(self): #create user and token
        user1=CustomUser.objects.create(phone='09121112233')
        user1.username='amir shiri'
        user1.save()
        token=CustomUserToken.objects.create(user_id=1,deviceId='sample',deviceType=1,validToken='sample',token='sample')
    def test_post_getphone(self): 
        url=reverse('get phone')
        data={'phone':'09303331122'}
        response=self.client.post(url,data) # create second user
        self.assertEqual(response.status_code,status.HTTP_201_CREATED) #201:user created
        self.assertEqual(CustomUser.objects.count(),2) # count should be 2
        self.assertEqual(CustomUser.objects.get(phone='09303331122').username,None) #username new user is none

    def test_post_signup(self):
        url=reverse('sign up') 
        data={'phone':'09121112233', #prepare data
            'deviceId':'sample',
            'validToken':'sample',
            'deviceType':'1'}
        response=self.client.post(url,data) #create user token and signup
        self.assertEqual(response.status_code,200) #token is update or create
        print(CustomUserToken.objects.get(user_id=1).token) # show new token

    def test_put_updateprofile(self):
        self.client=RequestsClient() # set APIclient to request client(because set headers)
        data={'username':'amir amir','phone':'09121112233'} #set data
        headers={"userId":"1","token":"sample"} # set headers
        response=self.client.put('http://localhost:8000/user/api/updateprofile',data=data,headers=headers)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT) #update done
        self.assertEqual(CustomUser.objects.get(pk=1).username,'amir amir') # check updated username
        t=CustomUserToken.objects.get(user_id=1)
        self.assertEqual(t.token,'sample') #check token

    def test_put_setNotify(self):
        self.client=RequestsClient()
        data={'notification_status':'true','phone':'09121112233'} #set data
        headers={'userId':'1','token':'sample'} #set headers
        self.client.head=headers
        response=self.client.put('http://localhost:8000/user/api/setNotificationStatus',data,headers=headers)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT) #update done
        self.assertEqual(CustomUser.objects.get(pk=1).notification_status,True) #check new notification status

    def test_logout(self):
        self.client=RequestsClient()
        headers={'userId':'1','token':'sample'}
        response=self.client.get('http://localhost:8000/user/api/logout',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_200_OK) #get the record
        response=self.client.put('http://localhost:8000/user/api/logout',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_200_OK) #update(log out) Done
        self.assertEqual(CustomUserToken.objects.get(pk=1).token,'None') # check updated token


        