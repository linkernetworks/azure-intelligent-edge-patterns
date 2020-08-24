# -*- coding: utf-8 -*-
"""
Azure Training Iteration Serializers
"""

import logging

from rest_framework import serializers

from ..models import TrainingIteration

logger = logging.getLogger(__name__)


class TrainingIterationSerializer(serializers.ModelSerializer):
    """TrainingIterationSerializer.
    """

    class Meta:
        """Meta.
        """

        model = TrainingIteration
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        """If object exist, project be read_only."""
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('project').read_only = True
