import graphene
from graphene_django.types import DjangoObjectType 
from cinemalog.models import Video,Competition,Question,UserAnswer,News

class VideoType(DjangoObjectType):
    message=graphene.String() # use to send msg
    class Meta:
        model=Video

class CompetitionType(DjangoObjectType):
    question=graphene.JSONString()  # list questions
    message=graphene.String()
    class Meta:
        model=Competition

class QuestionType(DjangoObjectType):
    message=graphene.String()  # use to send msg
    class Meta:
        model=Question

class UserAnswerType(DjangoObjectType):
    message=graphene.String()
    class Meta:
        model=UserAnswer

class NewsType(DjangoObjectType):
    message=graphene.String()  # use to send msg
    class Meta:
        model=News
        