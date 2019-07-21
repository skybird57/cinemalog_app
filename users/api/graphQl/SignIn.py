import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    status=graphene.Boolean()
    class Meta:
        model=get_user_model()


class Query(graphene.AbstractType):
    userList=graphene.List(UserType)
    userDetail=graphene.Field(UserType,
        username=graphene.String())
        #password=graphene.String())
    #use for authentication, show you are logined or not
    userLogin=graphene.Field(UserType)

    def resolve_userList(self,info):
        return get_user_model().objects.all()
    def resolve_userDetail(self,info,username):
        if username is not None:
            try:
                u= get_user_model().objects.get(username=username)
                u.status=True
            except Exception as e:
                print(e)
            
        return u
    #show user which is loginned
    def resolve_userLogin(self,info):
        user=info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user

