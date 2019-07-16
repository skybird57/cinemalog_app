from rest_framework import mixins,generics
from rest_framework import permissions
from cinemalog.models import Video
from cinemalog.Api.rest.serializers import VideoSerializer
from cinemalog.Api.rest.permissions import IsOwnerOrReadOnly


class Video_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class Video_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


#highlight
from rest_framework import renderers
from rest_framework.response import Response

class VideoHighlight(generics.GenericAPIView):
    queryset = Video.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        video = self.get_object()
        return Response(video.film_name)