# -*- coding: utf-8 -*-
"""App Signals
"""

import logging

from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from ..voe_projects.models import Project
from .models import Part

logger = logging.getLogger(__name__)
