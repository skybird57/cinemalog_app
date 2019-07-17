import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


# create type of table
class UserType(DjangoObjectType):
    class Meta:
        model=get_user_model()


class Query(graphene.AbstractType):
    userList=graphene.List(UserType)
    userDetail=graphene.Field(UserType,id=graphene.Int())
    #use for authentication, show you are logined or not
    userLogin=graphene.Field(UserType)

    def resolve_userList(self,info):
        return get_user_model().objects.all()
    def resolve_userDetail(self,info,id):
        if id is not None:
            return get_user_model().objects.get(pk=id)
    #show user which is loginned
    def resolve_userLogin(self,info):
        user=info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user

class UserInput(graphene.InputObjectType):
    username=graphene.String()
    email=graphene.String()
    password=graphene.String()

class CreateUser(graphene.Mutation):
    user=graphene.Field(UserType)
    class Arguments:
        input=UserInput()

    def mutate(self,info,input):
        user_instance=get_user_model()(
            username=input.username,
            email=input.email,
            password=input.password
        )
        user_instance.save()
        return CreateUser(user=user_instance)

class Mutation(graphene.ObjectType):
    create_user=CreateUser.Field()