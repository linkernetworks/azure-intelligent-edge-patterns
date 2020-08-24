# -*- coding: utf-8 -*-
"""App Models.
"""

import logging
import uuid as uuid_lib

from django.db import models
from django.utils.timezone import now

from voe_training.voe_projects.models import Project

logger = logging.getLogger(__name__)

# Create your models here.


class TrainingIteration(models.Model):
    """Training iterations Model
    """

    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
        unique=True)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                to_field='uuid',
                                null=True)
    performance = models.CharField(max_length=2000, default="{}")
    result_model = models.FileField(upload_to='models', null=True)
    timestamp = models.DateTimeField(default=now)
