import graphene
import graphql_jwt
from cinemalog.Api.GraphQL.schemaSendPush import Query as query_sendpush
from cinemalog.Api.GraphQL.schemaSendPush import Mutation as mutate_sendpush
from cinemalog.Api.GraphQL.schemaApplication import Query as query_application
from cinemalog.Api.GraphQL.schemaApplication import Mutation as mutate_application
from users.api.graphQl.schema import Query as query_user
from users.api.graphQl.schema import Mutation as mutation_user
class Query(query_user,query_sendpush,query_application,graphene.ObjectType):
    pass

class Mutation(mutation_user,mutate_sendpush,mutate_application,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)