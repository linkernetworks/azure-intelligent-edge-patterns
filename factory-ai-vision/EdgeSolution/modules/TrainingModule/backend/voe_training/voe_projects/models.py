# -*- coding: utf-8 -*-
"""App Models.

Include Project, Train and Task.
"""

import logging

from django.db import models
from django.db.models.signals import post_save, pre_save

from ..voe_settings.models import Setting

logger = logging.getLogger(__name__)


class Project(models.Model):
    """Project Model
    """

    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True, default="")
    download_uri = models.CharField(max_length=1000,
                                    null=True,
                                    blank=True,
                                    default="")
    training_counter = models.IntegerField(default=0)

    @staticmethod
    def pre_save(**kwargs):
        """pre_save.

        Args:
            kwargs:
        """
        logger.info("Project pre_save")
        if "sender" not in kwargs or kwargs["sender"] is not Project:
            return
        if "instance" not in kwargs:
            return
        if "update_fields" not in kwargs:
            return

        instance = kwargs["instance"]
        logger.info("Saving instance: %s", instance)
        logger.info("Project pre_save... End")

    @staticmethod
    def post_save(created, update_fields, **kwargs):
        """Project post_save
        """
        logger.info("Project post_save")

        if "sender" not in kwargs or kwargs["sender"] is not Project:
            return
        if "instance" not in kwargs:
            return

    @staticmethod
    def pre_delete(sender, instance, using):
        """pre_delete"""

    def dequeue_iterations(self, max_iterations=2):
        """Dequeue training iterations of a project"""

    def train_project(self):
        """
        Submit training task to CustomVision.
        Return training task submit result (boolean)
        : Success: return True
        : Failed : return False
        """
        logger.info("Training")
    
    def train(self):
        """
        Submit training task to CustomVision.
        Return training task submit result (boolean)
        : Success: return True
        : Failed : return False
        """
        self.train_project()

    def export_iterationv3_2(self, iteration_id):
        """export_iterationv3_2.

        Args:
            iteration_id:
        """
        # Export model to media
        # update self.download_uri


pre_save.connect(Project.pre_save, Project, dispatch_uid="Project_pre")
post_save.connect(Project.post_save, Project, dispatch_uid="Project_post")
