# -*- coding: utf-8 -*-
"""App Models."""

import logging

from django.db import models

logger = logging.getLogger(__name__)

# Create your models here.


class Setting(models.Model):
    """
    A wrapper model of CustomVisionTraingClient.

    Try not to pass CustomVisionTraingClient object if new model is expected to
    be created. e.g. create project, create train/iteration, etc.
    Instead, create a wrapper methods and let call, in order to sync the db
    with remote.
    """

    name = models.CharField(max_length=100,
                            blank=True,
                            default="",
                            unique=True)
    endpoint = models.CharField(max_length=1000, blank=True)
    training_key = models.CharField(max_length=1000, blank=True)
    iot_hub_connection_string = models.CharField(max_length=1000, blank=True)
    device_id = models.CharField(max_length=1000, blank=True)
    module_id = models.CharField(max_length=1000, blank=True)

    is_collect_data = models.BooleanField(default=False)

    is_trainer_valid = models.BooleanField(default=False)
    obj_detection_domain_id = models.CharField(max_length=1000,
                                               blank=True,
                                               default="")
    app_insight_has_init = models.BooleanField(default=False)

    class Meta:
        unique_together = ("endpoint", "training_key")

    def __str__(self):
        return self.name
