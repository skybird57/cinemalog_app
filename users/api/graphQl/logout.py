import graphene
from users.models import CustomUserToken
from users.Api.GraphQl.types import TokenType
import re # regex check mobile format

class Query(graphene.ObjectType):
    logout=graphene.Field(TokenType,  # make type
                        deviceId=graphene.String(),   # inputs
                        token=graphene.String())
    def resolve_logout(self,info,deviceId,token): # resolve_token 
        try:           
            token_instance=CustomUserToken.objects.get(token=token) # get token
            token_instance.token="None"   # update token to null
            token_instance.save()
            return token_instance  # return token
        except CustomUserToken.DoesNotExist:
            raise Exception("token is not valid")

