import graphene
from graphene_django import DjangoObjectType
from cinemalog.models import SendAdv


class SendAdvType(DjangoObjectType):
    class Meta:
        model=SendAdv

class Query(graphene.ObjectType):
    sendAdvs=graphene.List(SendAdvType)
    sendAdv_detail=graphene.Field(SendAdvType,id=graphene.Int())

    def resolve_sendAdvs(self,info):
        return SendAdv.objects.all()
    def resolve_sendAdv_detail(elf,info,id):
        if id is not None:
            return SendAdv.objects.get(pk=id)

class SendAdvInput(graphene.InputObjectType):
    title=graphene.String()
    content=graphene.String()
    adv_type=graphene.String()
    link=graphene.String()
    platform_android=graphene.Boolean()
    platform_ios=graphene.Boolean()
    pic=graphene.String()
class CreateAdv(graphene.Mutation):
    sendadv=graphene.Field(SendAdvType)
    class Arguments:
        input=SendAdvInput()

    def mutate(self,info,input):
        sendadv_instance=SendAdv(
            title=input.title,
            content=input.content,
            adv_type=input.adv_type,
            link=input.link,
            platform_android=input.platform_android,
            platform_ios=input.platform_ios,
            pic=DoFile(info,sendadv_instance).copyfile()
        )
        sendadv_instance.save()
        return CreateAdv(sendadv=sendadv_instance)

class UpdateAdv(graphene.Mutation):
    sendadv=graphene.Field(SendAdvType)
    class Arguments:
        id=graphene.Int()
        input=SendAdvInput()

    def mutate(self, info,id,input):
        sendadv_instance=SendAdv.objects.get(pk=id)
        if not sendadv_instance:
            raise Exception("id is invalid")
        sendadv_instance.title=input.title
        sendadv_instance.content=input.content
        sendadv_instance.platform_android=input.platform_android
        sendadv_instance.platform_ios=input.platform_ios
        sendadv_instance.save()
        return UpdateAdv(sendadv=sendadv_instance)

class DestroyAdv(graphene.Mutation):
    sendadv=graphene.Field(SendAdvType)
    class Arguments:
        id=graphene.Int()
    
    def mutate(self, info,id):
        sendadv_instance=SendAdv.objects.get(pk=id)
        if not sendadv_instance:
            raise Exception("id is invalid")
        sendadv_instance.delete()
        return DestroyAdv(sendadv=sendadv_instance)

class Mutation(graphene.ObjectType):
    create_sendadv=CreateAdv.Field()
    update_sendadv=UpdateAdv.Field()
    destroy_sendadv=DestroyAdv.Field()

class DoFile():
    def __init__(self,info,instance, *args, **kwargs):
        self.info=info
        self.instance=instance
    def copyfile(self):
        from django.core.files.storage import FileSystemStorage
        from Cinemalogs.settings import ROOT_ADV 
        fs=FileSystemStorage(location=ROOT_ADV+'\\'+str(instance.pic))
        pic=info.FILES['pic']
        instance.pic=fs.save(pic.name,pic)
        return instance.pic
    def removefile(self):
        pass
