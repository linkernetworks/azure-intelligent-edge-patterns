# -*- coding: utf-8 -*-
"""Vision on Edge Part Factories
"""

from factory import DjangoModelFactory, Faker, post_generation

from voe_training.voe_parts.models import Part


class PartFactory(DjangoModelFactory):
    """PartFactory.
    """

    name = Faker("name")
    description = Faker("sentence")

    class Meta:
        """Meta.
        """

        model = Part
        django_get_or_create = ["name"]
