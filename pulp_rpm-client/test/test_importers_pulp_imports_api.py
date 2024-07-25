# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.api.importers_pulp_imports_api import ImportersPulpImportsApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestImportersPulpImportsApi(unittest.TestCase):
    """ImportersPulpImportsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.importers_pulp_imports_api.ImportersPulpImportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_importers_core_pulp_imports_create(self):
        """Test case for importers_core_pulp_imports_create

        Create a pulp import  # noqa: E501
        """
        pass

    def test_importers_core_pulp_imports_delete(self):
        """Test case for importers_core_pulp_imports_delete

        Delete a pulp import  # noqa: E501
        """
        pass

    def test_importers_core_pulp_imports_list(self):
        """Test case for importers_core_pulp_imports_list

        List pulp imports  # noqa: E501
        """
        pass

    def test_importers_core_pulp_imports_read(self):
        """Test case for importers_core_pulp_imports_read

        Inspect a pulp import  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
