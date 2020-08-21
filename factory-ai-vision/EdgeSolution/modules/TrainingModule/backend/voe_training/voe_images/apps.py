# -*- coding: utf-8 -*-
"""Images App
"""

import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class ImagesConfig(AppConfig):
    """Vision on Edge Training App Config
    """

    name = 'voe_training.voe_images'

    def ready(self):
        """
        Images App Ready
        """
        # pylint: disable = unused-import, import-outside-toplevel
        from . import signals
