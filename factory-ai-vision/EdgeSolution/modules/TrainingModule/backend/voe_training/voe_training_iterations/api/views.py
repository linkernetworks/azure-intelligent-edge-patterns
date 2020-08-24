# -*- coding: utf-8 -*-
"""App views
"""

from __future__ import absolute_import, unicode_literals

import logging

from filters.mixins import FiltersMixin
from rest_framework import filters, viewsets

from ..models import TrainingIteration
from .serializers import TrainingIterationSerializer

logger = logging.getLogger(__name__)


class TrainingIterationViewSet(FiltersMixin, viewsets.ModelViewSet):
    """TrainingIterationViewSet.

    Filters:
        project_id
    """

    queryset = TrainingIteration.objects.all()
    serializer_class = TrainingIterationSerializer
    lookup_field = 'uuid'
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {"project": "project__uuid"}
