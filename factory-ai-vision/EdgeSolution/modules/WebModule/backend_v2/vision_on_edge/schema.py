import graphene

from .locations.gql_actions import LocationQuery


class Query(
    graphene.ObjectType, LocationQuery,
):
    pass


schema = graphene.Schema(query=Query)
