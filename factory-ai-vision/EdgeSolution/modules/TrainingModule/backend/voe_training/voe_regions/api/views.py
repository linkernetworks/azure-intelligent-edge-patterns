# -*- coding: utf-8 -*-
"""App views
"""

from __future__ import absolute_import, unicode_literals

from filters.mixins import FiltersMixin
from rest_framework import filters, viewsets

from ..models import Region
from .serializers import RegionSerializer


# pylint: disable=too-many-ancestors
class RegionViewSet(FiltersMixin, viewsets.ModelViewSet):
    """Region ModelViewSet
    """

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'uuid'
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        "project_id": "project_id",
    }
