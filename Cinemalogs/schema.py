import graphene
import graphql_jwt
from cinemalog.AdminApi.GraphQl.schemaSendPush import Query as query_sendpush
from cinemalog.AdminApi.GraphQl.schemaSendPush import Mutation as mutate_sendpush

from cinemalog.AdminApi.GraphQl.schemaSendAdv import Query as query_sendadv
from cinemalog.AdminApi.GraphQl.schemaSendAdv import Mutation as mutate_sendadv

from cinemalog.Api.GraphQL.forceUpdate import Query as query_application
from cinemalog.AdminApi.GraphQl.adminschemaApplication import Mutation as mutate_application

from users.Api.GraphQl.SignIn import Query as login_user
from users.Api.GraphQl.schema import Mutation as mutation_user
class Query(login_user,query_sendpush,query_sendadv,query_application,graphene.ObjectType):
    pass

class Mutation(mutation_user,mutate_sendpush,mutate_sendadv,mutate_application,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)