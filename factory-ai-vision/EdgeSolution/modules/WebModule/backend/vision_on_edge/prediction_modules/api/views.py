"""App API views.
"""

from __future__ import absolute_import, unicode_literals

import logging

from rest_framework import filters, viewsets

from ..models import PredictionModule
from .serializers import PredictionModuleSerializer

logger = logging.getLogger(__name__)


# pylint: disable=too-many-ancestors
class PredictionModuleViewSet(viewsets.ModelViewSet):
    """PredictionModuleViewSet."""

    queryset = PredictionModule.objects.all()
    serializer_class = PredictionModuleSerializer
