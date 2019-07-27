from rest_framework.decorators import APIView # use in class argument
from rest_framework import status # use in returns
from rest_framework import permissions # use for class permission
from rest_framework.response import Response  # use for returns
from rest_framework.reverse import reverse # use for api root
from cinemalog.AdminApi.Rest import api_api
from cinemalog.AdminApi.Rest.permissions import check_permissions 


# this api is class bases

class SendPushList(APIView):
    #permission_classes=(permissions.IsAuthenticatedOrReadOnly)
    #list video ,create video

    def get(self,request,format=None):
        data=api_api.api_list()
        return Response(data)

    def post(self,request,format=None):
        if check_permissions(request.user,'cinemalog.add_sendpush'):
            data,stts=api_api.api_create(request.data,request.user)
            return Response(data,status=stts)
        return Response(data,status=status.HTTP_403_FORBIDDEN)    
class SendPush_Detail(APIView):
    # retrive, update,delete video
    def get(self,request,pk,format=None):
        data=api_api.api_detail(pk)
        return Response(data)

    def put(self,request,pk,format=None):
        if check_permissions(request.user,'cinemalog.change_sendpush'):
            data,stts=api_api.api_update(request.data,request.user,pk)
            return Response(data,status=stts)
        return Response('no permission to update',status=status.HTTP_403_FORBIDDEN)    

    def delete(self,request,pk,format=None):
        if check_permissions(request.user,'cinemalog.delete_sendpush'):
            stts=api_api.api_delete(pk)    
            return Response('Delete Done',status=stts)
        return Response('no permission to delete',status=status.HTTP_403_FORBIDDEN) 


class Api_Root(APIView):
    def get(self,request,format=None):
        return Response({
            'av_sendpush':reverse('av_sendpush list',request=request,format=format),
        })