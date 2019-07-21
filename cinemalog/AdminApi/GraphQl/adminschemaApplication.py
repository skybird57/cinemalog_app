import graphene
from graphene_django import DjangoObjectType
from cinemalog.models import ApplicationVersion


class AdminApplicationType(DjangoObjectType):
    class Meta:
        model=ApplicationVersion

class AppInput(graphene.InputObjectType):
    platform=graphene.Int()
    required_version=graphene.Float()
    last_version=graphene.Float()
    generated_at=graphene.String()
    user_id=graphene.Int()

class CreateApp(graphene.Mutation):
    app=graphene.Field(AdminApplicationType)
    class Arguments:
        input=AppInput()
    
    def mutate(self,info,input):
        app_instance=ApplicationVersion(
            platform=input.platform,
            required_version=input.required_version,
            last_version=input.last_version,
            generated_at=input.generated_at,
            user_id=info.context.user.id
        )
        app_instance.save()
        return CreateApp(app=app_instance)

class UpdateApp(graphene.Mutation):
    app=graphene.Field(AdminApplicationType)
    class Arguments:
        id=graphene.Int()
        input=AppInput()
    
    def mutate(self, info,id,input):
        app_instance=ApplicationVersion.objects.get(pk=id)
        if not app_instance:
            raise Exception("the id is invalid")
        
        app_instance.platform=input.platform
        app_instance.required_version=input.required_version
        app_instance.last_version=input.last_version
        app_instance.generated_at=input.generated_at  
        app_instance.save()
        return UpdateApp(app=app_instance)

class DestroyApp(graphene.Mutation):
    class Arguments:
        id=graphene.Int()
    app=graphene.Field(AdminApplicationType)
    def mutate(self,info,id):
        app_instance=ApplicationVersion.objects.get(pk=id)
        if not app_instance:
            raise Exception("id is invalid")
        app_instance.delete()
        return DestroyApp(app=app_instance)

class Mutation(graphene.ObjectType):
    createApp=CreateApp.Field()
    updateApp=UpdateApp.Field()
    destroyApp=DestroyApp.Field()
