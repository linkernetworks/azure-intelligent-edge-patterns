"""App.
"""

import logging
import sys

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class PredictionModulesConfig(AppConfig):
    """App Config."""

    name = "vision_on_edge.prediction_modules"

    def ready(self):
        """ready."""

        if "runserver" in sys.argv:
            # pylint: disable= import-outside-toplevel
            from .helpers import create_init_objects

            logger.info("App ready ready while running server")
            create_init_objects()

            logger.info("App ready end while running server")
