"""App models.
"""

import logging

from django.db import models

logger = logging.getLogger(__name__)


class PredictionModule(models.Model):
    """PredictionModule Model."""

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000, unique=True)
    endpoint = models.CharField(max_length=200)
    secure = models.BooleanField(default=True)
    headers = models.CharField(max_length=200)

    def __str__(self):
        return self.name
