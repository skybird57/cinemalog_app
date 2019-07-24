#packages
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
#class and functions
from cinemalog.Api.rest.serializers import VideoSerializer
from cinemalog.models import Video,VideoView
from users.Api.Rest.checkUserToken import checkUserToken

#list of videos
class VideoList(APIView):    
    def get(self, request,format=None):   
        userId=request.query_params.get('userid')  #get user
        token=request.query_params.get('token')   # get token
        if not checkUserToken(userId,token):  # check if ok
            return Response('Your user_id or token is invalid',status=status.HTTP_400_BAD_REQUEST)
        instance=Video.objects.all()   # get all records
        serializer_instance=VideoSerializer(instance,many=True)   # serialize all record
        return Response(serializer_instance.data,status=status.HTTP_200_OK)  # return all records
        
# videoDetails and increament video views
class VideoDetail(APIView):
    def get(self,request,id,format=None):
        userId=request.query_params.get('userid')  # get user
        token=request.query_params.get('token')  # get token
        if not checkUserToken(userId,token):   # check if ok
            return Response('Your user_id or token is invalid',status=status.HTTP_400_BAD_REQUEST)
        if id is not None:
            try:
                instance=Video.objects.get(pk=id)  # get record
                if videoViewIncreament(userId,instance.id):  #check is user view this video befor or not
                    instance.view+=1   # add number og view
                    instance.save()  # save updated record
 
                serializer_instance=VideoSerializer(instance) # serialize
                return Response(serializer_instance.data,status=status.HTTP_200_OK) # return record
                

            except Video.DoesNotExist:
                pass
        return Response ("Id is not valid",status=status.HTTP_400_BAD_REQUEST)  # if video id is invalid
    
from datetime import datetime  # use for viewAt field
def videoViewIncreament(userId,videoId):
    if userId and videoId is not None:  # check parameters
        try:
            videoView=VideoView.objects.get(user_id=userId,video_id=videoId) # if seen befor return false
            return False
        except Exception:
            videoView=VideoView(user_id=userId,video_id=videoId,viewAt=datetime.today())
            videoView.save()  #if not seen before create new record and register user and video and return true
            return True