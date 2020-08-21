# -*- coding: utf-8 -*-
"""App models
"""

import logging

from django.db import models
from django.db.models.signals import pre_save
from django.db.utils import IntegrityError

from voe_training.voe_projects.models import Project

logger = logging.getLogger(__name__)


class Part(models.Model):
    """Part Model
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True, default="")
    name_lower = models.CharField(max_length=200, default=str(name).lower())
    part_type = models.CharField(max_length=20, blank=True, default="Regular")

    class Meta:
        unique_together = ("name_lower", "project_id")

    def __str__(self):
        return self.name

    @staticmethod
    def pre_save(update_fields, **kwargs):
        """Part pre_save
        """
        instance = kwargs['instance']
        try:
            update_fields = []
            instance.name_lower = str(instance.name).lower()
            update_fields.append("name_lower")
        except IntegrityError as integrity_error:
            logger.error(integrity_error)
            raise integrity_error
        except:
            logger.exception("Unexpected Error in Part Presave")


pre_save.connect(Part.pre_save, Part, dispatch_uid="Part_pre")
