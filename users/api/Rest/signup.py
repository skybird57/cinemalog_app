from rest_framework.decorators import APIView #model api
from rest_framework.response import Response # return method
from rest_framework import status # response status url
from users.models import CustomUser,CustomUserToken #models
from users.Api.Rest.serializers import UserSerializer,UserTokenSerializer # serializers
import re # use regex for phone format
class SignUp(APIView):
    # get method
    def get(self,request,format=None):
        phone=request.query_params.get('phone') # get phone from request
        if not phone:
            return Response('parameter is not sent',status=status.HTTP_404_NOT_FOUND)# if param wong
        p=re.search('^(09|989)[0-3]{1}[0-9]{8}$',phone)  # phone format
        if not p:
            return Response("Phone format is wrong",status=status.HTTP_404_NOT_FOUND)
        try:
            user_instance=CustomUser.objects.get(phone=phone) # get user
            serializer_userinstance=UserSerializer(user_instance)  # serialize user
            if serializer_userinstance:
                id=serializer_userinstance.data['id'] # get user id
                try:
                    token_instance=CustomUserToken.objects.get(user_id=id)  # find user token
                    serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
                    if serializer_tokeninstance:
                        return Response(serializer_tokeninstance.data,status=status.HTTP_200_OK) #return token return Response()
                except CustomUserToken.DoesNotExist:
                    return Response("change method to register your phone and token",status=status.HTTP_400_BAD_REQUEST) #problem 
        except CustomUser.DoesNotExist:
            return Response("Fisrt send phone to register",status=status.HTTP_400_BAD_REQUEST) #problem

    def post(self,request,format=None):
        phone=request.query_params.get('phone') # get phone from request
        deviceId=request.query_params.get('deviceId')  # get device id from request
        validToken=request.query_params.get('validToken') # get valid token from rquest
        if not phone:
            return Response('parameter is not sent',status=status.HTTP_404_NOT_FOUND)# if param wong
        p=re.search('^(09|989)[0-3]{1}[0-9]{8}$',phone)  # phone format
        if not p:
            return Response("Phone format is wrong",status=status.HTTP_404_NOT_FOUND)
        d=re.search('^(0|1)$',deviceId)
        if not d:
            return Response("device id format is wrong",status=status.HTTP_404_NOT_FOUND)
        try:
            user_instance=CustomUser.objects.get(phone=phone) # get user
            serializer_userinstance=UserSerializer(user_instance)  # serialize user
            if serializer_userinstance:
                id=serializer_userinstance.data['id'] # get user id
            try:
                token_instance=CustomUserToken.objects.filter(user_id=id,deviceId=deviceId)  # find user token
                #update token
            except CustomUserToken.DoesNotExist:
                token_instance=createtoken(id,deviceId,validToken)   # create if not found
                serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
                if serializer_tokeninstance:
                    return Response(serializer_tokeninstance.data,status=status.HTTP_200_OK) #return token
                else:
                    return Response(serializer_tokeninstance.errors,status=status.HTTP_400_BAD_REQUEST) #problem
        except CustomUser.DoesNotExist:
            return Response("Fisrt send phone to register",status=status.HTTP_400_BAD_REQUEST) #problem
            

# create new token
import uuid
def createtoken(id,deviceId,validToken):
    try:
        token=CustomUserToken()
        token.token=uuid.uuid4().hex
        token.user_id=id
        token.deviceId=deviceId
        token.validToken=validToken
        token.save()
        return token 
    except Exception:
        return None
       