from rest_framework import generics
from cinemalog.models import Video
from cinemalog.Api.rest.serializers import VideoSerializer
from cinemalog.Api.rest.permissions import IsOwnerOrReadOnly
from rest_framework import permissions

# in this view use base auth

class Video_list(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class Video_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    permission_classes=(IsOwnerOrReadOnly,)
    queryset=Video.objects.all()
    serializer_class=VideoSerializer    




