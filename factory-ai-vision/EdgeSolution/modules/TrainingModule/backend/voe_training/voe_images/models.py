# -*- coding: utf-8 -*-
"""Models for images"""

import json
import logging
import uuid as uuid_lib
from io import BytesIO

import requests
from django.core import files
from django.db import models
from django.db.models.signals import pre_save
from rest_framework import status

from ..voe_projects.models import Project

logger = logging.getLogger(__name__)

# Create your models here.


class Image(models.Model):
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
    image = models.ImageField(upload_to="images/")
    remote_url = models.CharField(max_length=1000, null=True)

    def get_remote_image(self):
        """get_remote_image.

        Download image using remote url
        """

        try:
            if self.remote_url:
                resp = requests.get(self.remote_url)
                if resp.status_code != status.HTTP_200_OK:
                    raise requests.exceptions.RequestException
                bytes_io = BytesIO()
                bytes_io.write(resp.content)
                file_name = f"{self.remote_url.split('/')[-1]}"
                logger.info("Saving as name %s", file_name)

                self.image.save(file_name, files.File(bytes_io))
                bytes_io.close()
                self.save()
        except requests.exceptions.RequestException as request_err:
            # Probably wrong url
            raise request_err
        except Exception as unexpected_error:
            logger.exception("unexpected error")
            raise unexpected_error

