# -*- coding: utf-8 -*-
"""App Signals
"""

import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from voe_training.voe_training_status.models import TrainingStatus

from .models import Project

logger = logging.getLogger(__name__)


@receiver(signal=post_save,
          sender=Project,
          dispatch_uid="create_training_status_if_not_exist")
def create_training_status_if_not_exist_handler(**kwargs):
    """Project create change.

    If a Project is created, create a Train(Training Status) as well.
    """

    logger.info("Azure Project changed.")
    logger.info("Checking...")

    instance = kwargs['instance']
    created = kwargs['created']
    if created:
        TrainingStatus.objects.update_or_create(
            project_id=instance.id,
            defaults={
                "status": "ok",
                "log": "Status : Has not configured",
                "performance": ""
            },
        )
    logger.info("Signals end")
