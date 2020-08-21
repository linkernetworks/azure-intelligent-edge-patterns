"""Image Factories
"""

import factory
from factory import DjangoModelFactory, Faker, post_generation

from voe_training.azure_parts.tests.factories import PartFactory
from voe_training.azure_training.tests.factories import ProjectFactory
from voe_training.images.models import Image


class ImageFactory(DjangoModelFactory):
    """ImageFactory.
    """

    project = factory.SubFactory(ProjectFactory)
    part = factory.SubFactory(PartFactory)
    remote_url = Faker("image_url")

    class Meta:
        """Meta.
        """

        model = Image
        django_get_or_create = ["remote_url"]

    @post_generation
    def post(obj, *args, **kwargs):
        """post.

        Args:
            obj:
            args:
            kwargs:
        """
        obj.get_remote_image()
