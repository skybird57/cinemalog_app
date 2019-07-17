import graphene
from cinemalog.Api.GraphQL.schema import Query as query_sendpush
from cinemalog.Api.GraphQL.schema import Mutation as mutate_sendpush
class Query(query_sendpush,graphene.ObjectType):
    pass

class Mutation(mutate_sendpush,graphene.ObjectType):
    pass

schema=graphene.Schema(query=Query,mutation=Mutation)