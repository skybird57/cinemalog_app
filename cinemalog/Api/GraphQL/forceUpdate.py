import graphene
from graphene_django import DjangoObjectType
from cinemalog.models import ApplicationVersion

# list, detail api for updateforc
class ApplicationType(DjangoObjectType):
    status=graphene.Int() # to return what should user do
    message=graphene.String()  # give message to end user
    link=graphene.String() # update link
    class Meta:
        model=ApplicationVersion

class Query(graphene.ObjectType):
    applicatins=graphene.List(ApplicationType) #list of applications
    app_detail=graphene.Field(ApplicationType, # detail of specific application
        version=graphene.Float(),  # input
        platform=graphene.String()  # input
        )

    def resolve_applicatins(self,info):   # show all records order by platform
        return ApplicationVersion.objects.order_by('platform')
    def resolve_app_detail(self,info,version,platform):  # show specific record
        if version and platform is not None:
            # platform  1:android  2:ios
            update=ApplicationVersion.objects.filter(platform=platform).order_by('-last_version').first()
            if not update:  # check the record is valid or not
                raise Exception("inputs are invalid")
            if version<update.required_version:    # check version,change status and return
                update.status=1
                update.message="force to update"
                update.link="http:\\linkupdate"
            elif version== update.required_version: 
                update.status=2
                update.message="It's better to update"
                update.link="http:\\linkupdate"
            elif version==update.last_version:
                update.status=3
                update.message="It's ok"
                update.link=""
            return update