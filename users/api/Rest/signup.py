from rest_framework.decorators import APIView #model api
from rest_framework.response import Response # return method
from rest_framework import status # response status url
from users.models import CustomUser,CustomUserToken #models
from users.Api.Rest.serializers import UserSerializer,UserTokenSerializer # serializers
import re # use regex for phone format
class SignUp(APIView):
    # get method
    def get(self,request,format=None):
        phone=request.headers.get('phone') # get phone from request
        deviceType=request.headers.get('deviceType')  # get device type from request
        deviceId=request.headers.get('deviceId')  # get device id from request
        validToken=request.headers.get('validToken') # get valid token from rquest
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
                    token_instance=CustomUserToken.objects.get(user_id=id,deviceId=deviceId)  # find user token
                    serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
                    if serializer_tokeninstance:
                        return Response(serializer_tokeninstance.data,status=status.HTTP_200_OK) #return token return Response()
                except CustomUserToken.DoesNotExist:
                    return Response("change method to register your phone and token",status=status.HTTP_400_BAD_REQUEST) #problem 
        except CustomUser.DoesNotExist:
            return Response("Fisrt send phone to register",status=status.HTTP_400_BAD_REQUEST) #problem

    def post(self,request,format=None):
        phone=request.data.get('phone') # get phone from request
        deviceType=request.data.get('deviceType')  # get device type from request
        deviceId=request.data.get('deviceId')  # get device id from request
        validToken=request.data.get('validToken') # get valid token from rquest
        if not phone:
            return Response('parameter is not sent',status=status.HTTP_404_NOT_FOUND)# if param wong
        p=re.search('^(09|989)[0-3]{1}[0-9]{8}$',phone)  # phone format
        if not p:
            return Response("Phone format is wrong",status=status.HTTP_404_NOT_FOUND)
        d=re.search('^(0|1)$',deviceType)
        if not d:
            return Response("device type format is wrong",status=status.HTTP_404_NOT_FOUND)
        try:
            user_instance=CustomUser.objects.get(phone=phone) # get user
            serializer_userinstance=UserSerializer(user_instance)  # serialize user
            if serializer_userinstance:
                id=serializer_userinstance.data['id'] # get user id
            try:
                if not (id and deviceId and deviceType and validToken):
                    raise  Exception("inputs are not compeleted")
                token_instance=CustomUserToken.objects.get(user_id=id,deviceId=deviceId)  # find user token
                token_instance=updateToken(token_instance,deviceId,deviceType,validToken) #update token
                serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
                if serializer_tokeninstance:
                    return Response(serializer_tokeninstance.data,status=status.HTTP_200_OK) #return token
                else:
                    return Response(serializer_tokeninstance.errors,status=status.HTTP_400_BAD_REQUEST) #problem
            except CustomUserToken.DoesNotExist:
            
                token_instance=createToken(id,deviceType,deviceId,validToken)   # create if not found
                serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
                if serializer_tokeninstance:
                    return Response(serializer_tokeninstance.data,status=status.HTTP_200_OK) #return token
                else:
                    return Response(serializer_tokeninstance.errors,status=status.HTTP_400_BAD_REQUEST) #problem
        except CustomUser.DoesNotExist:
            return Response("Fisrt send phone to register",status=status.HTTP_400_BAD_REQUEST) #problem
            

# create new token
import uuid
def createToken(id,deviceType,deviceId,validToken):
    try:
        token=CustomUserToken()
        token.token=uuid.uuid4().hex
        token.user_id=id
        token.deviceType=deviceType
        token.deviceId=deviceId
        token.validToken=validToken
        token.save()
        return token 
    except Exception:
        return None
def updateToken(token,deviceId,deviceType,validToken):
    token.DEVICE_TYPE=deviceType
    token.deviceId=deviceId
    token.validToken=validToken
    token.token=uuid.uuid4().hex
    token.save()
    return token
