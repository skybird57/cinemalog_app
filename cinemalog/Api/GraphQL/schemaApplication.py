import graphene
from graphene_django import DjangoObjectType
from cinemalog.models import ApplicationVersion


class ApplicationType(DjangoObjectType):
    class Meta:
        model=ApplicationVersion

class Query(graphene.ObjectType):
    applicatins=graphene.List(ApplicationType)
    app_detail=graphene.Field(ApplicationType,id=graphene.Int())

    def resolve_applicatins(self,info):
        return ApplicationVersion.objects.all()
    def resolve_app_detail(self,info,id):
        if id is not None:
            return ApplicationVersion.objects.get(pk=id)

class AppInput(graphene.InputObjectType):
    platform=graphene.String()
    require_version=graphene.Int()
    last_version=graphene.Int()
    generated_at=graphene.String()
    user_id=graphene.Int()

class CreateApp(graphene.Mutation):
    app=graphene.Field(ApplicationType)
    class Arguments:
        input=AppInput()
    
    def mutate(self,info,input):
        app_instance=ApplicationVersion(
            platform=input.platform,
            require_version=input.require_version,
            last_version=input.last_version,
            generated_at=input.generated_at,
            user_id=info.context.user.id
        )
        app_instance.save()
        return CreateApp(app=app_instance)


class Mutation(graphene.ObjectType):
    createApp=CreateApp.Field()
    #updateApp=UpdateApp.Field()
    #destroyApp=DestroyApp.Field()
