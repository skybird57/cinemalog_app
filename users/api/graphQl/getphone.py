import graphene
import random
import re
from datetime import datetime # create new user    

from users.Api.GraphQl.types import UserType
from users.models import CustomUser


class GetPhone(graphene.Mutation):
    user=graphene.Field(UserType)
    class Arguments:
        phone=graphene.String(required=True)

    def mutate(self, info,phone):
        if phone is not None:
            p=re.search('^09[0-3]{1}[0-9]{8}$',phone)  # phone format
            if p:
                try:
                    instance=CustomUser.objects.get(phone=phone)
                    instance.verifyCode=random.randint(1000,9999)
                    instance.save()
                    return GetPhone(user=instance)
                except CustomUser.DoesNotExist:
                    instance=createuser(phone)
                    return GetPhone(user=instance)
            raise Exception("phone format is wrong") # phon format wrong
        raise Exception("parameter is not sent")  # error in parameter


class Mutation(graphene.ObjectType):
    getPhone=GetPhone.Field()
    


def createuser(phone):
    try:
        user=CustomUser()
        user.phone=phone
        user.verifyCode=random.randint(1000,9999)
        user.created_at=datetime.today()
        user.save()    
        return user
    except Exception:
        raise Exception("duplicate phone")