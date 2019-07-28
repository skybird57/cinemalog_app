import graphene
from datetime import datetime
#classes and functions
from users.models import CustomUser
from users.Api.GraphQl.types import UserType
from users.Api.Rest.checkUserToken import checkUserToken

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
        return UpdateProfile(user=instance)

class Mutation(graphene.ObjectType):
    updateProfile=UpdateProfile.Field()