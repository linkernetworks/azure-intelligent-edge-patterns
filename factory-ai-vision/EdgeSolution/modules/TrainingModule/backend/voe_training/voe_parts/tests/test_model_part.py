# -*- coding: utf-8 -*-
"""Vision on Edge Part Models testcases.
"""

from django.core.exceptions import MultipleObjectsReturned

from voe_training.general.tests.azure_testcase import CustomVisionTestCase
from voe_training.general.tests.test_special_strings import special_strings

from ..models import Part


class VoePartTestCase(CustomVisionTestCase):
    """AzurePartTestCase.

    Azure Part model testcases.
    """

    def setUp(self):

    def test_setup_is_valid(self):
        """
        Make sure setup is valid
        """

    def test_create_without_description(self):
        """
        Type:
            Positive

        Description:
            Try to create parts without description assigned.
            Description column is now not mandatory.

        Expected Results:
            Object created. Description is ''
        """
