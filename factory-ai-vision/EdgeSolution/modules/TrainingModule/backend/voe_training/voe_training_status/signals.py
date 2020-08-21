# -*- coding: utf-8 -*-
"""App Signals
"""

import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from voe_training.voe_training_status.models import TrainingStatus
from voe_training.notifications.models import Notification

logger = logging.getLogger(__name__)


@receiver(signal=post_save,
          sender=TrainingStatus,
          dispatch_uid="training_status_send_notification")
def training_status_send_notification_handler(**kwargs):
    """training_status_send_notification_handler.

    Args:
        kwargs:
    """
    instance = kwargs['instance']
    if 'need_to_send_notification' in dir(
            instance) and instance.need_to_send_notification:
        logger.info("VoE TrainingStatus changed.")
        logger.info("instance.need_to_send_notification %s",
                    instance.need_to_send_notification)
        Notification.objects.create(notification_type="project",
                                    sender="system",
                                    title=instance.status.capitalize(),
                                    details=instance.log.capitalize())
    logger.info("Signal end")
