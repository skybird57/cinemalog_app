import graphene
from users.models import CustomUserToken
from users.Api.GraphQl.types import TokenType
from users.Api.Rest.checkUserToken import checkUserToken

class Query(graphene.ObjectType):
    logout=graphene.Field(TokenType,  # make type
                        userId=graphene.Int(),   # inputs
                        token=graphene.String())
    def resolve_logout(self,info,userId,token): # resolve_token 
        if not checkUserToken(userId,token):
            raise Exception("user id or token is invalid")    
        try:           
            token_instance=CustomUserToken.objects.get(token=token) # get token
            token_instance.token="None"   # update token to null
            token_instance.save()  #save change
            return token_instance  # return token
        except CustomUserToken.DoesNotExist:
            raise Exception("token is not valid")
