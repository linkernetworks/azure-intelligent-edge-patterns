# -*- coding: utf-8 -*-
"""Conftest
"""

import pytest

from voe_training.notifications.models import Notification
from voe_training.notifications.tests.factories import NotificationFactory


@pytest.fixture
def notification() -> Notification:
    """notification.

    Args:

    Returns:
        Notification:
    """
    return NotificationFactory()
