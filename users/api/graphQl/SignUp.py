import graphene
from users.models import CustomUser,CustomUserToken
from users.Api.GraphQl.types import UserType,TokenType
import re # regex check mobile format

class Query(graphene.ObjectType):
    userSignUp=graphene.Field(TokenType,phone=graphene.String())
    
    def resolve_userSignUp(self,info,phone): # query_signup
        if phone is not None:
            p=re.search('^09[0-3]{1}[0-9]{8}$',phone)  # phone format
            if p:
                try:
                    user_instance= CustomUser.objects.get(phone=phone) # get user
                except CustomUser.DoesNotExist:
                    user_instance=createuser(phone)  # create user
                if user_instance:   # create=Done
                    id=user_instance.id   # get id
                    try:
                        token_instance=CustomUserToken.objects.get(user_id=id) # get token
                    except CustomUserToken.DoesNotExist:
                        token_instance=createtoken(id)   # create token if is invalid
                    return token_instance   #return token
                raise Exception("user is not created")  # cant create user
            raise Exception("phone format is wrong") # phon format wrong
        raise Exception("parameter is not sent")  # error in parameter

# create new user    
from datetime import datetime
def createuser(phone):
    try:
        user=CustomUser()
        user.phone=phone
        user.save()
        if createtoken(user.id):
            return user
    except Exception:
        raise Exception("duplicate phone")
# create new token
import uuid
def createtoken(id):
    try:
        token=CustomUserToken()
        token.token=uuid.uuid4().hex
        token.user_id=id
        token.save()
        return token    
    except Exception:
        raise Exception("duplicate token")