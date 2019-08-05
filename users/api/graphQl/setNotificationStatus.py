import graphene
from datetime import datetime
#classes and functions
from users.models import CustomUser
from users.Api.GraphQl.types import UserType
from users.Api.Rest.checkUserToken import checkUserToken

class UserStatusInput(graphene.InputObjectType):
    status=graphene.Boolean()
class SetNotificationStatus(graphene.Mutation):
    user=graphene.Field(UserType)
    class Arguments:
        userId=graphene.Int()
        token=graphene.String()
        input=UserStatusInput()
    def mutate(self,info,userId,token,input):
        if not checkUserToken(userId,token):
            raise Exception("user id or token is invalid")    
        instance=CustomUser.objects.get(pk=userId)
        instance.notification_status=input.status
        instance.updated_at=datetime.today()
        instance.save()
        return SetNotificationStatus(user=instance)

class Mutation(graphene.ObjectType):
    Setnotificationstatus=SetNotificationStatus.Field()
