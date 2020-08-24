"""
Models for azure prediction
"""

import uuid as uuid_lib
import logging

from django.db import models
from django.db.models.signals import pre_save

logger = logging.getLogger(__name__)


class ImagePrediction(models.Model):
    """Image Prediction"""
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
        unique=True)
    image = models.ImageField(upload_to="predictions/")
    predicted = models.BooleanField(default=False)

    @staticmethod
    def pre_save(**kwargs):
        """pre_save.

        Args:
            kwargs:
        """

        if 'instance' not in kwargs:
            logger.info("no instance given")
            return

        instance = kwargs['instacne']
        logger.info("Image Prediction Presave")
        if not instance.predicted:
            logger.info("Predictiing")
            # Do something here...


pre_save.connect(ImagePrediction.pre_save,
                 ImagePrediction,
                 dispatch_uid="ImagePrediction_pre")
