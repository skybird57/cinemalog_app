from cinemalog.Api.rest.serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from cinemalog.models import Video
from rest_framework import status,permissions


class VideoList(APIView):
    permission_class=(permissions.IsAuthenticatedOrReadOnly)
    def get(self, request,format=None):
        if  not request.query_params.get('id'):
            instance=Video.objects.all()
            serializer_instance=VideoSerializer(instance,many=True)
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            try:
                instance=Video.objects.get(pk=request.query_params.get('id'))
            except Video.DoesNotExist:
                instance= None
            serializer_instance=VideoSerializer(instance)
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)