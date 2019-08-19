from rest_framework.test import APITestCase,RequestsClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import CustomUser,CustomUserToken
from cinemalog.models import ApplicationVersion,Competition,Question,Video,VideoView,News,NewsView,Plan
from datetime import datetime

class CinemalogTest(APITestCase):
    def setUp(self): #create some records in alias
        User.objects.create_superuser(username='admin',email='aa@a.com',password='admin')
        CustomUser.objects.create(phone='09360001315')
        CustomUserToken.objects.create(user_id=1,deviceId='sample',deviceType=1,validToken='sample',token='sample')
        ApplicationVersion.objects.create(platform=1,required_version=3.2,
                last_version=3.6,generated_at=datetime.today(),user_id=1)
        Competition.objects.create(title='match 1',created_at=datetime.today(),user_id=1)
        Question.objects.create(question='q1',created_at=datetime.today(),user_id=1,
                    answer1='a1',answer2='a1',answer3='a1',answer4='a1',correct_answer=2,
                    score_ca=4,score_wa=-2,competition_id=1)
        Video.objects.create(film_name='hezarpa',desc='comic',user_id=1)
        Plan.objects.create(title='p1',typee=2,days=30,price='3000')

    def test_appversion(self):

        url=reverse('rest force update')  #get url name
        params={'version':'3','platform':'1'} # set parameters
        response=self.client.get(url,params) #send request
        print(response.data)
        self.assertEqual(response.data[1],'force update') # message should be 'force update'
    def test_videos(self):
        self.client=RequestsClient()  #set Apiclient to requestclient(because we want to set headers)
        headers={'userId':'1','token':'sample'} #set header
        response=self.client.get('http://localhost:8000/cinemalog/api/dialog',headers=headers) #send request
        self.assertEqual(response.status_code,status.HTTP_200_OK) #200:if responde video list
        v=Video.objects.get(pk=1) # get rec 1 from video
        self.assertEqual(v.film_name,'hezarpa')  #name should be 'hezarpa'
        response=self.client.get('http://localhost:8000/cinemalog/api/dialog/1',headers=headers) #view the (id)1 video
        self.assertEqual(response.status_code,status.HTTP_200_OK) #200: get record 1
        #print(response)
        self.assertEqual(VideoView.objects.count(),1) #vidoeview should have 1 record ^
    def test_competition(self):
        self.client=RequestsClient() #set Apiclient to request client(because to set headers)
        headers={'userId':'1','token':'sample'} #set headers
        response=self.client.get('http://localhost:8000/cinemalog/api/competition',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_200_OK) #200:get all record
        response=self.client.get('http://localhost:8000/cinemalog/api/competition/1',headers=headers)
        print(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK) #200:get specific record
    def test_questions(self):
        self.client=RequestsClient()#set Apiclient to request client(because to set headers)
        headers={'userId':'1','token':'sample','compId':'2'}#set headers
        response=self.client.get('http://localhost:8000/cinemalog/api/question',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_200_OK)#200:get all record
        response=self.client.get('http://localhost:8000/cinemalog/api/question/1',headers=headers)
        print(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)#200:get specific record
    def test_news(self):
        url=reverse('crawl news') #get url name
        response=self.client.get(url) # call crawl
        self.client=RequestsClient() #set Apiclient to request client(because to set headers)
        headers={'userId':'1','token':'sample'}#set headers
        response=self.client.get('http://localhost:8000/cinemalog/api/news',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_200_OK)#200:get all record
        n=News.objects.get(pk=1)
        self.assertEqual(n.view,0)#hich bazdidi az news1 nashodeh ast 
        response=self.client.get('http://localhost:8000/cinemalog/api/news/1',headers=headers)#az news1 bazdid shod
        self.assertEqual(response.status_code,status.HTTP_200_OK)#200:get specific record
        #print(response)
        self.assertEqual(News.objects.get(pk=1).view,1) # view news1 bayad 1 bashad chon 1 bazdid anjam shod
        self.assertEqual(NewsView.objects.count(),1) #count table bazdid 1 mishavad chon 1 bazdid anjam shod
    def test_plans(self):
        self.client=RequestsClient()#set Apiclient to request client(because to set headers)
        headers={'userId':'1','token':'sample'}#set headers
        response=self.client.get('http://localhost:8000/cinemalog/api/plans',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_200_OK)#200:get all record
        self.assertEqual(Plan.objects.count(),1) #1 record darim
        response=self.client.get('http://localhost:8000/cinemalog/api/userplan',headers=headers)
        #print(response)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)#user hich plani nadarad
        headers={'userId':'1','token':'sample','planId':'1'} #set post headers
        response=self.client.post('http://localhost:8000/cinemalog/api/userplan',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)#user 1 plan kharid
        response=self.client.post('http://localhost:8000/cinemalog/api/userplan',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)#user 2 plan kharid
        response=self.client.post('http://localhost:8000/cinemalog/api/userplan',headers=headers)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)#user mojaz be kharide bish az 2 plan nist

    def test_answer(self):
        print('user score befor answer:',CustomUser.objects.get(pk=1).score)#user score is 0
        self.client=RequestsClient() #set Apiclient to request client(because to set headers)
        headers={'userId':'1','token':'sample'}#set headers
        data={'answers': [{'cycle_question_id': '1',
                            'data': [{'question': '1',
                            'answer': '3'
                            }]
                        }]
            }
        response=self.client.post('http://localhost:8000/cinemalog/api/answer',json=data,headers=headers) 
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)#201: #register answer
        print('user score after answer:',CustomUser.objects.get(pk=1).score) #user score updated
        self.assertEqual(CustomUser.objects.get(pk=1).score,-2) #check user score
        