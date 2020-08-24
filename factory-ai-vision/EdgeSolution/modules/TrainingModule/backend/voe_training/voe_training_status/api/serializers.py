"""
Azure Training Status Serializers
"""

import logging

from rest_framework import serializers

from ..models import TrainingStatus

logger = logging.getLogger(__name__)


class TrainingStatusSerializer(serializers.ModelSerializer):
    """TrainingStatusSerializer.
    """

    class Meta:
        """Meta.
        """

        model = TrainingStatus
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        """If object exist, project be read_only."""
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('iteration').read_only = True
