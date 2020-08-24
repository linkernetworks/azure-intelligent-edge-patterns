# -*- coding: utf-8 -*-
"""App views.
"""

from __future__ import absolute_import, unicode_literals

from filters.mixins import FiltersMixin
from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from ..models import Part
from .serializers import PartSerializer


# pylint: disable=too-many-ancestors
class PartViewSet(FiltersMixin, viewsets.ModelViewSet):
    """PartViewSet.

    Args:
        partname (str): unique

    Filters:
        is_demo (bool)
    """

    queryset = Part.objects.all()
    serializer_class = PartSerializer
    lookup_field = 'uuid'
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        "project_id": "project_id",
    }


