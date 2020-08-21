# -*- coding: utf-8 -*-
"""Azure Part REST API testcases.
"""

import json
import logging

from django.urls import reverse
from rest_framework import status

from voe_training.general.tests.azure_testcase import CustomVisionTestCase
from voe_training.general.tests.test_special_strings import special_strings

from ..models import Part

logger = logging.getLogger(__name__)


class AzurePartRestTestCases(CustomVisionTestCase):
    """AzurePartRestTestCases.

    Azure Part REST API testcases.
    """

    def setUp(self):
        """setUp.
        """

    def test_setup_is_valid(self):
        """test_setup_is_valid.
        """

    def test_create_part(self):
        """test_create_part.

        Type:
            Positive

        Description:
            Ensure we can created a part by rest api.

        Expected Results:
            200 { 'name':'part_name', 'description':'part_description' }
        """

    def test_create_dup_parts(self):
        """
        Type:
            Negative

        Description:
            Ensure create duplicate Part objects will failed.

        Expected Results:
            400 { 'status': 'failed', 'log': 'xxx'}
        """

    def test_create_same_lowercase_parts(self):
        """test_create_same_lowercase_parts.

        Type:
            Negative

        Description:
            Ensure Part (name, is_demo) is unique together.

        Expected Results
            400 { 'status': 'failed', 'log': 'xxx' }
        """

    def test_create_no_desb_parts(self):
        """test_create_no_desb_parts.

        Type:
            Positive

        Description:
            Create a part without description assigned.
            Description column is not mandatory.

        Expected Results:
            201 { 'name': 'part_name', 'description': 'xxx' }
        """

    def test_create_demo_parts_with_same_name(self):
        """test_create_demo_parts_with_same_name.

        Type:
            Negative

        Description:
            Create demo part and none-demo part with same name.
            Should pass.

        Expected Results:
            pass
        """

    def test_create_demo_parts_with_same_name_2(self):
        """test_create_demo_parts_with_same_name_2.

        Type:
            Positive

        Description:
            Create parts with same name.

        Expected Results:
            Failed.
        """

    def test_put(self):
        """test_put.

        Type:
            Positive

        Description:
            Test update is ok.

        Expected Results:
            200 OK
        """
