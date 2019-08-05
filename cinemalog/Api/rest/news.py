#packages
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
#class and functions
from cinemalog.Api.rest.serializers import NewsSerializer
from cinemalog.models import News,NewsView
from users.Api.Rest.checkUserToken import checkUserToken

#list of News
class NewsList(APIView):    
    def get(self, request,format=None):   
        userId=request.query_params.get('userId')  #get user
        token=request.query_params.get('token')   # get token
        if not checkUserToken(userId,token):  # check if ok
            return Response('Your user_id or token is invalid',status=status.HTTP_400_BAD_REQUEST)
        instance=News.objects.all()   # get all records
        serializer_instance=NewsSerializer(instance,many=True)   # serialize all record
        return Response(serializer_instance.data,status=status.HTTP_200_OK)  # return all records
        
# videoDetails and increament video views
class NewsDetail(APIView):
    def get(self,request,id,format=None):
        userId=request.query_params.get('userId')  # get user
        token=request.query_params.get('token')  # get token
        if not checkUserToken(userId,token):   # check if ok
            return Response('Your user_id or token is invalid',status=status.HTTP_400_BAD_REQUEST)
        if id is not None:
            try:
                instance=News.objects.get(pk=id)  # get record
                if newsViewIncreament(userId,instance.id):  #check if user view this news befor or not
                    instance.view+=1   # add number og view
                    instance.save()  # save updated record
 
                serializer_instance=NewsSerializer(instance) # serialize
                return Response(serializer_instance.data,status=status.HTTP_200_OK) # return record
            except News.DoesNotExist:
                pass
        return Response ("News Id is not valid",status=status.HTTP_400_BAD_REQUEST)  # if news id is invalid
    
from datetime import datetime  # use for viewAt field
def newsViewIncreament(userId,newsId):
    if userId and newsId is not None:  # check parameters
        try:
            newsView=NewsView.objects.get(user_id=userId,news_id=newsId) # if seen befor return false
            return False
        except Exception:
            newView=NewsView(user_id=userId,news_id=newsId,viewAt=datetime.today())
            newView.save()  #if not seen before create new record and register user and video and return true
            return True