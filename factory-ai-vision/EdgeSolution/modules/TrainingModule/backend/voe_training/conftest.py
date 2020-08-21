"""Conftest
"""

import pytest

from voe_training.azure_parts.models import Part
from voe_training.azure_parts.tests.factories import PartFactory
from voe_training.azure_settings.models import Setting
from voe_training.azure_settings.tests.factories import SettingFactory
from voe_training.azure_training.models import Project
from voe_training.azure_training.tests.factories import ProjectFactory
from voe_training.azure_training_status.models import TrainingStatus
from voe_training.azure_training_status.tests.factories import \
    TrainingStatusFactory
from voe_training.images.models import Image
from voe_training.images.tests.factories import ImageFactory
from voe_training.locations.models import Location
from voe_training.locations.tests.factories import LocationFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """media_storage.

    Args:
        settings:
        tmpdir:
    """
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def setting() -> Setting:
    """setting.

    Args:

    Returns:
        Setting:
    """
    return SettingFactory()


@pytest.fixture
def project() -> Project:
    """project.

    Args:

    Returns:
        Project:
    """
    return ProjectFactory()


@pytest.fixture
def status() -> TrainingStatus:
    """status.

    Args:

    Returns:
        TrainingStatus:
    """
    return TrainingStatusFactory()


@pytest.fixture
def location() -> Location:
    """location.

    Args:

    Returns:
        Location:
    """
    return LocationFactory()


@pytest.fixture
def part() -> Part:
    """part.

    Args:

    Returns:
        Part:
    """
    return PartFactory()


@pytest.fixture
def image() -> Image:
    """image.

    Args:

    Returns:
        Image:
    """
    return ImageFactory()
