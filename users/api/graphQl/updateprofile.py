import graphene
from datetime import datetime
#classes and functions
from users.models import CustomUser
from users.Api.GraphQl.types import UserType
from users.Api.Rest.checkUserToken import checkUserToken
# use file storage
import random
from django.core.files.storage import FileSystemStorage
from Cinemalogs import settings

class UserInput(graphene.InputObjectType):
    username=graphene.String()
class UpdateProfile(graphene.Mutation):
    user=graphene.Field(UserType)
    class Arguments:
        userId=graphene.Int()
        token=graphene.String()
        input=UserInput()
    def mutate(self,info,userId,token,input):
        if not checkUserToken(userId,token):
            raise Exception("user id or token is invalid")    
        instance=CustomUser.objects.get(pk=userId)
        instance.username=input.username
        instance.updated_at=datetime.today()
        instance.save()
        try:
            avatar=info.context.FILES['photo']
            print('avataaaaaaaaaaaaaaaaaar',info.context.FILES['photo'])
            uploadUserImage(instance,avatar)
        except Exception:
            pass
        instance.save()
        return UpdateProfile(user=instance)

class Mutation(graphene.ObjectType):
    updateProfile=UpdateProfile.Field()


def uploadUserImage(inctance,avatar):
    avatarname=str.split(avatar.name,'.') # split file name and add random number tofirst part of name to avoid duplicate
    avatar.name=avatarname[0]+'_'+str(random.randint(112,99992))+'.'+avatarname[len(avatarname)-1]#attach file extention
    print('avataaaaaaaaaaaaar',avatar.name)
    fs=FileSystemStorage(location=settings.MEDIA_ROOT+'/avatar/') # define location
    inctance.image=fs.save(avatar.name,avatar) # save in image record
    inctance.save() # save serializer