from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime  
#classes & functions
from users.Api.Rest.serializers import UserSerializer
from users.models import CustomUser
from users.Api.Rest.checkUserToken import checkUserToken
#upload pic
from django.core.files.storage import FileSystemStorage
from Cinemalogs import settings
import random

class UpdateProfile(APIView):  # get record
    def get(self,request,format=None):
        try:
            instance=CustomUser.objects.get(pk=request.headers.get('userId')) # get user
            serializer_instance=UserSerializer(instance)
            return Response(serializer_instance.data,status=status.HTTP_200_OK) #show user
        except CustomUser.DoesNotExist: 
            return Response("user id is not valid",status=status.HTTP_404_NOT_FOUND) # show error
    
    def put(self,request,format=None):  # update function
        userId=request.headers.get('userId')   # get parameters
        token=request.headers.get('token')
        if not userId:
            raise Exception("user id is not sent")
        if not checkUserToken(userId,token):   # check permission
            raise Exception("user id or token is invalid")
        instance=CustomUser.objects.get(pk=userId) #get user record
        serializer_inctance=UserSerializer(instance,data=request.data)  # srialize with new data
        if serializer_inctance.is_valid():
            serializer_inctance.save(updated_at=datetime.today())  # update with new data
            try:
                avatar=request.data['image']               # get image file
                uploadUserImage1(serializer_inctance,avatar) # copy image file to DIR and update image field
            except Exception:
                pass 
            return Response(serializer_inctance.data,status=status.HTTP_204_NO_CONTENT)  # return updated record
        else:
            return Response(serializer_inctance.errors,status=status.HTTP_400_BAD_REQUEST) #return errors
# use file storage
def uploadUserImage1(serializer_inctance,avatar):
    avatarname=str.split(avatar.name,'.') # split file name and add random number tofirst part of name to avoid duplicate
    avatar.name=avatarname[0]+'_'+str(random.randint(112,99992))+'.'+avatarname[len(avatarname)-1]#attach file extention
    print('avataaaaaaaaaaaaar',avatar.name)
    fs=FileSystemStorage(location=settings.MEDIA_ROOT+'/avatar/') # define location
    serializer_inctance.image=fs.save(avatar.name,avatar) # save in image record
    serializer_inctance.save() # save serializer

# use open file
from django.core.files import File
def uploadUserImage2(serializer_inctance,avatar):
    avatarname=str.split(avatar.name,'.')
    avatar.name=avatarname[0]+'_'+str(random.randint(112,99992))+'.'+avatarname[len(avatarname)-1]
    print('avataaaaaaaaaaaaar',avatar.name)
    location=settings.MEDIA_ROOT+'/avatar/'+avatar.name
    file = open(location, "wb")
    with open(avatar, "rb") as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            file.write(byte[0])
    file.closed
    f.closed
    serializer_inctance.image=avatar.name
    serializer_inctance.save()
