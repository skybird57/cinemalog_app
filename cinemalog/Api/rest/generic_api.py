from rest_framework import generics
from cinemalog.models import Video
from cinemalog.Api.rest.serializers import VideoSerializer


class Video_list(generics.ListCreateAPIView):
    
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class Video_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer    




