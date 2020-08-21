# -*- coding: utf-8 -*-
"""App
"""

import logging
import sys

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class VoePartsConfig(AppConfig):
    """App Config

    Import models and signals and create some demo objects
    """

    name = 'voe_training.voe_parts'

    def ready(self):
        """ready
        """
        if 'runserver' in sys.argv:
            # Import models in migrate/makemigration will occurs error.
            # pylint: disable = import-outside-toplevel
            # pylint: disable = unused-import

            from voe_training.voe_parts import signals
            logger.info("Part App Config end while running server")
