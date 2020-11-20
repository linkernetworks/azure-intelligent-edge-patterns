"""App model tests.
"""

from rest_framework.test import APITransactionTestCase

from ..models import PredictionModule


class PredictionModuleTestCase(APITransactionTestCase):
    """PredictionModuleTestCase.

    App Model testcases.
    """

    def setUp(self):
        """setUp."""
        PredictionModule.objects.create(name="PredictionModule1", url="localhost:5000")
