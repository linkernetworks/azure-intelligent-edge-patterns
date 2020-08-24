# -*- coding: utf-8 -*-
"""App Config
"""

import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class RegionsConfig(AppConfig):
    """Vision on Edge Training App Config
    """

    name = 'voe_training.voe_regions'

    def ready(self):
        """
        Images App Ready
        """
        # pylint: disable = unused-import, import-outside-toplevel
        from . import signals
