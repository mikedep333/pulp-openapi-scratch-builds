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
import datetime

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.pulp_import_check import PulpImportCheck  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestPulpImportCheck(unittest.TestCase):
    """PulpImportCheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PulpImportCheck
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.pulp_import_check.PulpImportCheck()  # noqa: E501
        if include_optional :
            return PulpImportCheck(
                path = '0', 
                toc = '0', 
                repo_mapping = '0'
            )
        else :
            return PulpImportCheck(
        )

    def testPulpImportCheck(self):
        """Test PulpImportCheck"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
