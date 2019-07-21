from cinemalog.models import SendPush
from cinemalog.Api.rest.serializers import SendpushSerializer
from rest_framework import status
from rest_framework.response import Response

def api_list():
    instance=SendPush.objects.all()
    serializer_instance=SendpushSerializer(instance,many=True)
    return serializer_instance.data

def api_create(data,user):
    serializer_instance=SendpushSerializer(data=data)
    if serializer_instance.is_valid():
        serializer_instance.save(user=user)
        return serializer_instance.data, status.HTTP_201_CREATED   
    return serializer_instance.errors,status.HTTP_400_BAD_REQUEST

def get_record(pk):
    try:
        instance=SendPush.objects.get(pk=pk)
    except SendPush.DoesNotExist:
        return None
    return instance    

def api_detail(pk):
    instance=get_record(pk)
    if not instance:
        return '404---- the id is invalid'
    serializer_instance=SendpushSerializer(instance)
    return serializer_instance.data    

def api_update(data,user,pk):
    instance=get_record(pk)
    if not instance:
        return '404---- the id is invalid'
    serializer_instance=SendpushSerializer(instance,data=data)
    if serializer_instance.is_valid():
        serializer_instance.save(user=user)
        return serializer_instance.data,status.HTTP_202_ACCEPTED
    return serializer_instance.errors,status.HTTP_400_BAD_REQUEST

def api_delete(pk):
    instance=get_record(pk)
    if not instance:
        return '404---- the id is invalid'
    instance.delete()
    return status.HTTP_204_NO_CONTENT  