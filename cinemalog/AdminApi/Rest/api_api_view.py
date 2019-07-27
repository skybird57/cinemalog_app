
from rest_framework.decorators import api_view # use befor defs
from rest_framework.response import Response  # use in returns
from rest_framework.reverse import reverse # use in api_root
from rest_framework import status # use in returns
from cinemalog.AdminApi.Rest import api_api 
from cinemalog.AdminApi.Rest.permissions import check_permissions 


@api_view(['GET','POST'])
def api_sendpush_list(request,format=None):
    
    if request.method=='GET':
        data=api_api.api_list()
        return Response(data)
    elif request.method=='POST':
        if check_permissions(request.user,'cinemalog.add_sendpush'):
            data,stts=api_api.api_create(request.data,request.user)
            return Response(data,status=stts)
        return Response(data,status=status.HTTP_403_FORBIDDEN)    
        

@api_view(['GET','PUT','DELETE'])
def api_sendpush_detail(request,pk,format=None):
    if request.method=='GET':
        data=api_api.api_detail(pk)
        return Response(data)

    elif request.method=='PUT':
        if check_permissions(request.user,'cinemalog.change_sendpush'):
            data,stts=api_api.api_update(request.data,request.user,pk)
            return Response(data,status=stts)
        else:
            return Response('no permission to update',status=status.HTTP_403_FORBIDDEN)

    elif request.method=='DELETE':
        if check_permissions(request.user,'cinemalog.delete_sendpush'):
            stts=api_api.api_delete(pk)
            return Response('Delete Done',status=stts)
        else:
            return Response('no permission to delete',status=status.HTTP_403_FORBIDDEN)

# create api_root
@api_view(['GET'])
def api_api_root(request,format=None):
    rootlinks={
        'a_sendpush':reverse(api_sendpush_list,request=request,format=format),
    }
    return Response(rootlinks)