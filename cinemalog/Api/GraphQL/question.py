import graphene
from cinemalog.Api.GraphQL.types import QuestionType
from cinemalog.models import Question,Competition
from users.Api.Rest.checkUserToken import checkUserToken

class Query(graphene.ObjectType):
    questions=graphene.List(QuestionType,  #*args
                        userId=graphene.Int(), #**kwargs
                        token=graphene.String())  #**kwargs
    question_detail=graphene.Field(QuestionType,
                        id=graphene.Int(),
                        userId=graphene.Int(),#**kwargs
                        token=graphene.String())#**kwargs

    def resolve_questions(self,info,**kwargs):
        userId=kwargs.get('userId') # get kwargs
        token=kwargs.get('token')
        if not checkUserToken(userId,token):  # check user token
            raise Exception("Your user_id or token is invalid")
        instance=Question.objects.all()  # get all records
        return instance  # return all records

    def resolve_question_detail(self,info,id,**kwargs):
        userId=kwargs.get('userId')  # get kwargs
        token=kwargs.get('token')
        if not checkUserToken(userId,token):  # check user token
            raise Exception("Your user_id or token is invalid")
        if id is not None:  # check id question
            try:
                instance=Question.objects.get(pk=id)  # get record   
            except Question.DoesNotExist:
                raise Exception("ID is invalid")
        return instance  # return specific record