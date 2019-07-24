import graphene
from graphene_django.types import DjangoObjectType
from users.models import CustomUser,CustomUserToken
class UserType(DjangoObjectType):  
    class Meta:
        model=CustomUser

class TokenType(DjangoObjectType):
    class Meta:
        model=CustomUserToken