from graphene_django.types import DjangoObjectType 
from cinemalog.models import Video,Question

class VideoType(DjangoObjectType):
    class Meta:
        model=Video

class QuestionType(DjangoObjectType):
    class Meta:
        model=Question