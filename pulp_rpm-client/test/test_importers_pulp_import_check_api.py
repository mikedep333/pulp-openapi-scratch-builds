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
from pulpcore.client.pulp_rpm.api.importers_pulp_import_check_api import ImportersPulpImportCheckApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestImportersPulpImportCheckApi(unittest.TestCase):
    """ImportersPulpImportCheckApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.importers_pulp_import_check_api.ImportersPulpImportCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pulp_import_check_post(self):
        """Test case for pulp_import_check_post

        Validate the parameters to be used for a PulpImport call  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
