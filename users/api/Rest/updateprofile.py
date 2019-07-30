from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
#classes & functions
from users.Api.Rest.serializers import UserSerializer
from users.models import CustomUser
from users.Api.Rest.checkUserToken import checkUserToken

class UpdateProfile(APIView):
    def get(self,request,format=None):
        instance=CustomUser.objects.filter(pk=request.query_params.get('userId'))
        serializer_instance=UserSerializer(instance[0])
        return Response(serializer_instance.data)
    def put(self,request,format=None):
        userId=request.query_params.get('userId')
        token=request.query_params.get('token')
        if not checkUserToken(userId,token):
            raise Exception("user id or token is invalid")
        instance=CustomUser.objects.get(pk=request.query_params.get('userId'))
        serializer_inctance=UserSerializer(instance,data=request.data)
        if serializer_inctance.is_valid():
            serializer_inctance.save(updated_at=datetime.today())
            return Response(serializer_inctance.data,status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer_inctance.errors,status=status.HTTP_400_BAD_REQUEST)