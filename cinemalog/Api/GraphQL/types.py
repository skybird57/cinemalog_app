import graphene
from graphene_django.types import DjangoObjectType 
from cinemalog.models import Video,Question,News

class VideoType(DjangoObjectType):
    message=graphene.String() # use to send msg
    class Meta:
        model=Video

class QuestionType(DjangoObjectType):
    message=graphene.String()  # use to send msg
    class Meta:
        model=Question

class NewsType(DjangoObjectType):
    message=graphene.String()  # use to send msg
    class Meta:
        model=News
        