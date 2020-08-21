# -*- coding: utf-8 -*-
"""App"""

import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)

DEFAULT_SETTING_NAME = 'DEFAULT_SETTING'


class VoeSettingsConfig(AppConfig):
    """AppConfig"""

    name = 'voe_training.voe_settings'
