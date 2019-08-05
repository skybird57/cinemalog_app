from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime  
#classes & functions
from users.Api.Rest.serializers import UserSerializer
from users.models import CustomUser
from users.Api.Rest.checkUserToken import checkUserToken


class SetNotificationStatus(APIView):  # get record
    def get(self,request,format=None):
        try:
            instance=CustomUser.objects.get(pk=request.query_params.get('userId')) # get user
            serializer_instance=UserSerializer(instance)
            return Response(serializer_instance.data,status=status.HTTP_200_OK) #show user
        except CustomUser.DoesNotExist: 
            return Response("user id is not valid",status=status.HTTP_400_BAD_REQUEST) # show error
    
    def put(self,request,format=None):  # update function
        userId=request.query_params.get('userId')   # get parameters
        token=request.query_params.get('token')
        
        if not checkUserToken(userId,token):   # check permission
            raise Exception("user id or token is invalid")
        instance=CustomUser.objects.get(pk=request.query_params.get('userId')) #get user record
        serializer_inctance=UserSerializer(instance,data=request.data)  # srialize with new data
        if serializer_inctance.is_valid():
            serializer_inctance.save(updated_at=datetime.today())  # update with new data
            return Response(serializer_inctance.data,status=status.HTTP_204_NO_CONTENT)  # return updated record
        else:
            return Response(serializer_inctance.errors,status=status.HTTP_400_BAD_REQUEST) #return errors
