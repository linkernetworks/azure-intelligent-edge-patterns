"""App API serializers.
"""

import logging

from rest_framework import serializers

from ..models import PredictionModule

logger = logging.getLogger(__name__)


class PredictionModuleSerializer(serializers.ModelSerializer):
    """PredictionModuleSerializer"""

    class Meta:
        model = PredictionModule
        fields = "__all__"
