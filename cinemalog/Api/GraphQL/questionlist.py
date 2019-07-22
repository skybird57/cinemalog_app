import graphene
from cinemalog.Api.GraphQL.types import QuestionType
from cinemalog.models import Question

class Query(graphene.ObjectType):
    questions=graphene.List(QuestionType)
    question_detail=graphene.Field(QuestionType,id=graphene.Int())

    def resolve_questions(self,info):
        instance=Question.objects.all()
        return instance

    def resolve_question_detail(self,info,id):
        try:
            if id is not None:
                instance=Question.objects.get(pk=id)
        except Question.DoesNotExist:
            instance=None
        return instance