# -*- coding: utf-8 -*-
"""App views
"""

from __future__ import absolute_import, unicode_literals

from filters.mixins import FiltersMixin
from rest_framework import filters, viewsets

from ..models import Image
from .serializers import ImageSerializer


# pylint: disable=too-many-ancestors
class ImageViewSet(FiltersMixin, viewsets.ModelViewSet):
    """Image ModelViewSet
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'uuid'
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        "project_id": "project_id",
    }
