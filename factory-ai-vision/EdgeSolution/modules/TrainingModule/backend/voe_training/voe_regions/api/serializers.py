# -*- coding: utf-8 -*-
"""App Serializers
"""

import logging

from rest_framework import serializers

from ..models import Region

logger = logging.getLogger(__name__)


class RegionSerializer(serializers.ModelSerializer):
    """RegionSerializer"""

    class Meta:
        model = Region
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        """If object exist, project be read_only."""
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('project').read_only = True
            self.fields.get('image').read_only = True

    def validate(self, attrs):
        """Make sure part and image belongs to same project"""
        if attrs['part'] is not None and attrs['part'].project.uuid != attrs[
                'project'].uuid:
            raise serializers.ValidationError(
                {'error': 'part should belongs to region project'})
        if attrs['image'] is not None and attrs['image'].project.uuid != attrs[
                'project'].uuid:
            raise serializers.ValidationError(
                {'error': 'image should belongs to region project'})
        return attrs
