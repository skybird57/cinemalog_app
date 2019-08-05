from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUserToken
from users.Api.Rest.serializers import UserTokenSerializer
from users.Api.Rest.checkUserToken import checkUserToken
class Logout(APIView):
    def get(self,request,format=None):
        deviceId=request.query_params.get('deviceId')  # get device id from request
        token=request.query_params.get('token') # get token from rquest
        try:
            token_instance=CustomUserToken.objects.get(token=token)  # find user token
            serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
            if serializer_tokeninstance:
                return Response(serializer_tokeninstance.data,status=status.HTTP_200_OK) #return token return Response()
            else:
                return Response(serializer_tokeninstance.errors,status=status.HTTP_400_BAD_REQUEST) #problem
        except CustomUserToken.DoesNotExist:
            return Response("device id or token is invalid",status=status.HTTP_400_BAD_REQUEST) #problem 
    
    def put(self,request,format=None):
        userId=request.query_params.get('userId')  # get device id from request
        token=request.query_params.get('token') # get token from rquest
        if not checkUserToken(userId,token):   # check permission
            raise Exception("user id or token is invalid")
        try:
            token_instance=CustomUserToken.objects.get(token=token)  # find user token
            token_instance.token="None"
            token_instance.save()
            serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
            if serializer_tokeninstance:
                return Response(serializer_tokeninstance.data,status=status.HTTP_200_OK) #return token return Response()
            else:
                return Response(serializer_tokeninstance.errors,status=status.HTTP_400_BAD_REQUEST) #problem
        except CustomUserToken.DoesNotExist:
            return Response("device id or token is invalid",status=status.HTTP_400_BAD_REQUEST) #problem 
        

