"""App graphql actions.
"""

import graphene

from .gql_types import LocationType
from .models import Location


class LocationQuery:
    location = graphene.Field(LocationType, id=graphene.UUID())
    locations = graphene.List(LocationType, id=graphene.UUID(), name=graphene.String())

    def resolve_location(self, info, **kwargs):
        return Location.objects.filter(id=kwargs.get("id")).first()

    def resolve_locations(self, info, **kwargs):
        qs = Location.objects.all()
        return qs.filter(**kwargs)
