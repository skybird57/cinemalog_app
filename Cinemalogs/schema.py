import graphene
import graphql_jwt
#import Api Queries
from cinemalog.Api.GraphQL.forceUpdate import Query as query_application #its ok
from cinemalog.Api.GraphQL.dialog import Query as query_video #its ok
from cinemalog.Api.GraphQL.news import Query as query_news # its ok
from users.Api.GraphQl.SignUp import Query as query_signup #its ok

#import AdminApi Queries
from cinemalog.AdminApi.GraphQl.schemaSendPush import Query as query_sendpush
from cinemalog.AdminApi.GraphQl.schemaSendPush import Mutation as mutate_sendpush
from cinemalog.AdminApi.GraphQl.schemaSendAdv import Query as query_sendadv
from cinemalog.AdminApi.GraphQl.schemaSendAdv import Mutation as mutate_sendadv
from cinemalog.AdminApi.GraphQl.adminschemaApplication import Mutation as mutate_application
#import Api Mutations
#from cinemalog.Api.GraphQL.dialog import Mutation as mutate_videoViewInc
#from users.Api.GraphQl.SignIn import Query as login_user
#from users.Api.GraphQl.schema import Mutation as mutation_user
#import AdminApi Mutations


class Query(query_signup,
            query_video,
            query_news,
            query_sendpush,
            query_sendadv,
            query_application,
            graphene.ObjectType):
    pass

class Mutation(mutate_sendpush,
                mutate_sendadv,
                mutate_application,
                graphene.ObjectType):
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)