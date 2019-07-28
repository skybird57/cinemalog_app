import graphene
#classes and functions
from cinemalog.models import Competition,Question
from cinemalog.Api.GraphQL.types import CompetitionType
from users.Api.Rest.checkUserToken import checkUserToken
class Query(graphene.ObjectType):
    competitions=graphene.List(CompetitionType,          #for all records
                                userId=graphene.Int(),
                                token=graphene.String())
    competition_detail=graphene.Field(CompetitionType,    # for single record
                                id=graphene.Int(),
                                userId=graphene.Int(),
                                token=graphene.String())
    def resolve_competitions(self,info,**kwargs):    # get all records
        userId=kwargs.get('userId')
        token=kwargs.get('token')
        if not checkUserToken(userId,token):   # check permission
            raise Exception("userid or token is invalid")
        instance=Competition.objects.order_by('-id')
        for item in instance:      # for each competition get all questions
            item.question=Question.objects.filter(competition_id=item.id)
        return instance
    
    def resolve_competition_detail(self,info,id,**kwargs):        # get single record
        userId=kwargs.get('userId')
        token=kwargs.get('token')
        if not checkUserToken(userId,token):     # check permission
            raise Exception("userid or token is invalid")
        try:
            instance=Competition.objects.get(pk=id)   # get record
        except Exception:
            raise Exception("competition Id is invalid")
        return instance
