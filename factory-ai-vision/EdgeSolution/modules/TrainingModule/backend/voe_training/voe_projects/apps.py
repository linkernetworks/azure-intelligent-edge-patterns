# -*- coding: utf-8 -*-
"""App"""

import logging
import sys

from django.apps import AppConfig

logger = logging.getLogger(__name__)

class VoeProjectConfig(AppConfig):
    """App Config

    Import signals and create demo objects.
    """

    name = 'voe_training.voe_projects'

    def ready(self):
        """
        Azure Training App Ready
        """
        if 'runserver' in sys.argv:
            # pylint: disable=unused-import, import-outside-toplevel
            logger.info("ready while running server")
            logger.info("Importing Signals")
            from . import signals
            logger.info("Azure Training AppConfig End while running server")
            # pylint: enable=unused-import, import-outside-toplevel
