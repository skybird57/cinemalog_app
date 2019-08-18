#packages
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status,permissions
#classes and functions
from cinemalog.Api.rest.serializers import CompetitionSerializer
from cinemalog.models import Competition
from users.Api.Rest.checkUserToken import checkUserToken

class CompetitionList(APIView):
    def get(self, request,format=None):   #get all records
        userid=request.headers.get('userId') #get user id
        token=request.headers.get('token') #get token
        if not checkUserToken(userid,token): # check token
             return Response('Your user_id or token is invalid',status=status.HTTP_401_UNAUTHORIZED)        
        instance=Competition.objects.order_by('-id') # get all records order by id
        serializer_instance=CompetitionSerializer(instance,many=True) # serialize data
        return Response(serializer_instance.data,status=status.HTTP_200_OK)  # return all records
        
class CompetitionDetail(APIView):
    def get(self,request,id,format=None):    # get one record
        userid=request.headers.get('userId')  #get user id
        token=request.headers.get('token')  # get token
        if not checkUserToken(userid,token):  # check token
             return Response('Your user_id or token is invalid',status=status.HTTP_401_UNAUTHORIZED)
        if id is not None:    
            try:
                instance=Competition.objects.get(pk=id)  # try to get specific record
                serializer_instance=CompetitionSerializer(instance)  # serialize record
                return Response(serializer_instance.data,status=status.HTTP_200_OK)  # return record
            except Competition.DoesNotExist:
                pass
        return Response("Competition ID is invalid",status=status.HTTP_400_BAD_REQUEST)  # id invalid