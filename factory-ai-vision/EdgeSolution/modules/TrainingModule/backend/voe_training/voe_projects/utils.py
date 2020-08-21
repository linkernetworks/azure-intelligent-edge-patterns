# -*- coding: utf-8 -*-
"""Project Utilities
"""

import logging

from voe_training.azure_app_insight.utils import get_app_insight_logger
from voe_training.voe_parts.models import Part
from voe_training.general import error_messages
from voe_training.voe_images.models import Image

from .models import Project

logger = logging.getLogger(__name__)


def update_app_insight_counter(
        project_obj,
        has_new_parts: bool,
        has_new_images: bool,
        parts_last_train: int,
        images_last_train: int,
):
    """Send message to app insight"""
