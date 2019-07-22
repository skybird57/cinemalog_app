import graphene
from cinemalog.Api.GraphQL.types import VideoType
from cinemalog.models import Video

class Query(graphene.ObjectType):
    videos=graphene.List(VideoType)
    video_detail=graphene.Field(VideoType,id=graphene.Int())

    def resolve_videos(self,info):
        instance=Video.objects.all()
        return instance

    def resolve_video_detail(self,info,id):
        try:
            if id is not None:
                instance=Video.objects.get(pk=id)
        except Video.DoesNotExist:
            instance=None
        return instance