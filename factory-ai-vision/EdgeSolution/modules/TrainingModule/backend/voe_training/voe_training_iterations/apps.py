# -*- coding: utf-8 -*-
"""App"""

import logging
import sys

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class VoeTrainingIterationConfig(AppConfig):
    """App Config

    Import signals and create demo objects.
    """

    name = 'voe_training.voe_training_iterations'

    def ready(self):
        """
        Vision on Edge Training Iteration App Ready
        """
        if 'runserver' in sys.argv:
            # pylint: disable=unused-import, import-outside-toplevel
            from . import signals
