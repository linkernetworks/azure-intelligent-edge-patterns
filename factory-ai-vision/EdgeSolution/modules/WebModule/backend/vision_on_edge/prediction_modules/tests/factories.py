"""App model factories.
"""

from factory import DjangoModelFactory, Faker

from ..models import PredictionModule


class PredictionModuleFactory(DjangoModelFactory):
    """PredictionModuleFactory."""

    name = Faker("name")
    url = Faker("url")

    class Meta:
        model = PredictionModule
        django_get_or_create = ["url"]
