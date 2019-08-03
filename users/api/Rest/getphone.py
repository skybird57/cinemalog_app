from rest_framework.decorators import APIView #model api
from rest_framework.response import Response # return method
from rest_framework import status # response status url
import re # use regex for phone format
import random
#classes and functions
from users.models import CustomUser,CustomUserToken #models
from users.Api.Rest.serializers import UserSerializer,UserTokenSerializer # serializers

class getphone(APIView): 
    def get(self,request,format=None):
        phone=request.query_params.get('phone') # get phone from request
        if not phone:
            return Response('parameter is not sent',status=status.HTTP_404_NOT_FOUND)# if param wong
        p=re.search('^(09|989)[0-3]{1}[0-9]{8}$',phone)  # phone format
        if not p:
            return Response("Phone format is wrong",status=status.HTTP_404_NOT_FOUND)
        try:
            user_instance=CustomUser.objects.get(phone=phone)
            serializer_instance=UserSerializer(user_instance)
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response("user is invalid change you request method",status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,format=None):
        phone=request.query_params.get('phone') # get phone from request
        if not phone:
            return Response('parameter is not sent',status=status.HTTP_404_NOT_FOUND)# if param wong
        p=re.search('^(09|989)[0-3]{1}[0-9]{8}$',phone)  # phone format
        if not p:
            return Response("Phone format is wrong",status=status.HTTP_404_NOT_FOUND)
        try:
            user_instance=CustomUser.objects.get(phone=phone)
            user_instance.verifyCode=random.randint(1000,9999)
            user_instance.save()
            serializer_instance=UserSerializer(user_instance)
            return Response(serializer_instance.data,status=status.HTTP_204_NO_CONTENT) # get user if register before
        except CustomUser.DoesNotExist:
            user_instance=createuser(phone)    # create user if not exist
            serializer_instance=UserSerializer(user_instance)
            if serializer_instance:
                return Response(UserSerializer.data,status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)

# create new user 
from datetime import datetime   
def createuser(phone):
        user=CustomUser()
        user.phone=phone
        user.verifyCode=random.randint(1000,9999)
        user.created_at=datetime.today()
        user.save()
        return user