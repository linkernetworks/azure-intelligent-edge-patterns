# -*- coding: utf-8 -*-
"""App Models"""

import json
import logging
import uuid as uuid_lib

from django.db import models
from django.db.models.signals import pre_save
from rest_framework.serializers import ValidationError

from ..voe_projects.models import Project
from ..voe_parts.models import Part
from ..voe_images.models import Image

logger = logging.getLogger(__name__)

# Create your models here.


class Region(models.Model):
    """Image.

    models.Model
    """

    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
        unique=True)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                to_field='uuid')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, to_field='uuid')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, to_field='uuid')
    labels = models.CharField(max_length=1000, null=True)
    confidence = models.FloatField(default=0.0)

    @staticmethod
    def pre_save(**kwargs):
        """pre_save.

        Args:
            instance:
            kwargs:
        """
        instance = kwargs['instance']
        if (instance.part.project != instance.project or
                instance.image.project != instance.project):
            raise ValidationError(
                "Part and Image should belong to this project")


pre_save.connect(Region.pre_save, Region, dispatch_uid="Region_pre_save")
