from cinemalog.Api.rest.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from cinemalog.models import Question
from rest_framework import status,permissions
from users.Api.Rest.checkUserToken import checkUserToken

class QuestionList(APIView):
    def get(self, request,format=None):
        userid=request.query_params.get('userid')
        token=request.query_params.get('token')
        if not checkUserToken(userid,token):
             return Response('Your user_id or token is invalid',status=status.HTTP_400_BAD_REQUEST)        
        instance=Question.objects.all()
        serializer_instance=QuestionSerializer(instance,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
        
class QuestionDeatail(APIView):
    def get(self,request,id,format=None):
        userid=request.query_params.get('userid')
        token=request.query_params.get('token')
        if not checkUserToken(userid,token):
             return Response('Your user_id or token is invalid',status=status.HTTP_400_BAD_REQUEST)
        if id is not None:    
            try:
                instance=Question.objects.get(pk=id)
                serializer_instance=QuestionSerializer(instance)
                return Response(serializer_instance.data,status=status.HTTP_200_OK)
            except Question.DoesNotExist:
                pass
        return Response("ID is invalid",status=status.HTTP_400_BAD_REQUEST)