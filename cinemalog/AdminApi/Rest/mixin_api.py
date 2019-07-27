from rest_framework import mixins,generics
from rest_framework import permissions,authentication
from cinemalog.models import Video
from cinemalog.AdminApi.Rest.serializers import VideoSerializer
from cinemalog.AdminApi.Rest.permissions import IsOwnerOrReadOnly

# in this view user token auth

class Video_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    authentication_class=(authentication.TokenAuthentication,)
    #permission_classes=(permissions.IsAuthenticated,)
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class Video_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    authentication_class=(authentication.TokenAuthentication,)
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
