"""App utilities.

Utilities does not depends on models.
If a function depends on models, place it in helpers.py.
"""

import logging

from .models import Location

logger = logging.getLogger(__name__)


def create_demo_objects():
    """create_demo_objects.
    """
    logger.info("Creating demo objects.")
    Location.objects.update_or_create(
        name="Demo Location", is_demo=True, defaults={"description": "Demo Location"},
    )
