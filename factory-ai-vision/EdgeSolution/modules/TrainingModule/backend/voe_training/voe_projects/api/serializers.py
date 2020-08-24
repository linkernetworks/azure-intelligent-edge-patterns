# -*- coding: utf-8 -*-
"""Vision on Edge Serializers
"""

import logging

from rest_framework import serializers

from voe_training.voe_projects.models import Setting
from voe_training.voe_projects.models import Project

logger = logging.getLogger(__name__)


class ProjectSerializer(serializers.ModelSerializer):
    """Project Serializer"""

    class Meta:
        model = Project
        exclude = ['id']
        extra_kwargs = {
            "setting": {
                "required": False
            },
            "download_uri": {
                "required": False
            },
        }

    def __init__(self, *args, **kwargs):
        """If object exist, project be read_only."""
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('setting').read_only = True
