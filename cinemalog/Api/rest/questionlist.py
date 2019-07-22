from cinemalog.Api.rest.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from cinemalog.models import Question
from rest_framework import status,permissions


class QuestionList(APIView):
    permission_class=(permissions.IsAuthenticatedOrReadOnly)
    def get(self, request,format=None):
        if  not request.query_params.get('id'):
            instance=Question.objects.all()
            serializer_instance=QuestionSerializer(instance,many=True)
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            try:
                instance=Question.objects.get(pk=request.query_params.get('id'))
            except Question.DoesNotExist:
                instance= None
            serializer_instance=QuestionSerializer(instance)
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)