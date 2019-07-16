from cinemalog.Api.rest.serializers import ApplicationVersionSerializer
from cinemalog.models import ApplicationVersion
from django.http import HttpResponse

def check_permission(user,permission):
    print(user)
    if user.is_authenticated:
        print(user.get_all_permissions)
        if permission in  user.get_all_permissions:
            return True
        else: 
            return False

#list of videos        
def json_list():
        instance=ApplicationVersion.objects.all()
        serializer_instance=ApplicationVersionSerializer(instance,many=True)
        return serializer_instance.data
   
#create new video
def json_create(data,user):
    serializer_instance=ApplicationVersionSerializer(data=data)
    if serializer_instance.is_valid():
        serializer_instance.save(user=user)
        return serializer_instance.data
    return serializer_instance.errors

# get video for detail,update,delete
def get_record(pk):
    try:
        instance=ApplicationVersion.objects.get(pk=pk)
    except ApplicationVersion.DoesNotExist:
        return None
    return instance

# video detail
def json_detail(pk): 
    instance=get_record(pk) 
    if  not instance:  
        return '404---- the id is invalid'
    serializer_instance=ApplicationVersionSerializer(instance)
    return serializer_instance.data
            

# video update
def json_update(data,user,pk):
    instance=get_record(pk)
    if  not instance:  
        return '404---- the id is invalid'

    serializer_instance=ApplicationVersionSerializer(instance,data=data)
    if serializer_instance.is_valid():
        serializer_instance.save(user=user)
        return serializer_instance.data
    return serializer_instance.errors

#delete video
def json_delete(request,pk):
    instance=get_record(pk)
    if  not instance:  
        return '404---- the id is invalid'
    #from Cinemalogs.settings import MEDIA_ROOT,MEDIA_URL
    #import shutil
    ##delete files and folders
    #try:   
    #    path=MEDIA_ROOT+'\\MEDIA_ROOT\\'+video_instance.film_name
    #    shutil.rmtree(path)
    #except OSError as e:
    #    pass        
    #delete record
    instance.delete()
    return '204---delete is done'    

    