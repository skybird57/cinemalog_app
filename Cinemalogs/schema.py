import graphene
import graphql_jwt
#cinemalog
#import Api Queries
from cinemalog.Api.GraphQL.forceUpdate import Query as query_application #its ok
from cinemalog.Api.GraphQL.dialog import Query as query_video #its ok
from cinemalog.Api.GraphQL.competition import Query as query_competition #it's ok
from cinemalog.Api.GraphQL.question import Query as query_question #it's ok
from cinemalog.Api.GraphQL.news import Query as query_news # its ok
#import AdminApi Queries
from cinemalog.AdminApi.GraphQl.schemaSendPush import Query as query_sendpush
from cinemalog.AdminApi.GraphQl.schemaSendPush import Mutation as mutate_sendpush
from cinemalog.AdminApi.GraphQl.schemaSendAdv import Query as query_sendadv
from cinemalog.AdminApi.GraphQl.schemaSendAdv import Mutation as mutate_sendadv
from cinemalog.AdminApi.GraphQl.adminschemaApplication import Mutation as mutate_application
#import Api Mutations
from cinemalog.Api.GraphQL.answer import Mutation as answer_register

#Users
#import Api Queries
from users.Api.GraphQl.logout import Query as logout
#import Api Mutations
from users.Api.GraphQl.getphone import Mutation as getphone
from users.Api.GraphQl.SignUp import Mutation as signup #its ok
from users.Api.GraphQl.updateprofile import Mutation as update_profile

class Query(logout,query_video,  
            query_competition,
            query_question,
            query_news,
            query_sendpush,
            query_sendadv,
            query_application,
            graphene.ObjectType):
    pass

class Mutation(getphone, #create user
                signup, # create token
                update_profile,  # update user
                answer_register,
                mutate_sendpush,
                mutate_sendadv,
                mutate_application,
                graphene.ObjectType):
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)