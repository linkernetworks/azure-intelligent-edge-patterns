# -*- coding: utf-8 -*-
"""App Serializers
"""

import logging

from rest_framework import serializers

from ..models import Image

logger = logging.getLogger(__name__)


class ImageSerializer(serializers.ModelSerializer):
    """ImageSerializer"""

    class Meta:
        model = Image
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        """If object exist, project be read_only."""
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('project').read_only = True
