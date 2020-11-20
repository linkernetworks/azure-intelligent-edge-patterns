"""App REST API Test
"""

from rest_framework.test import APITransactionTestCase

from ..models import PredictionModule


class PredictionModuleRestTestCases(APITransactionTestCase):
    """PredictionModuleRestTestCases

    PredictionModule REST API testcases.
    """

    def setUp(self):
        """setUp."""
        PredictionModule.objects.create(name="PredictionModule1", url="localhost:5000")

    def test_setup_is_valid(self):
        """test_setup_is_valid.

        Make sure setup is valid
        """
        self.assertEqual(PredictionModule.objects.count(), 1)
