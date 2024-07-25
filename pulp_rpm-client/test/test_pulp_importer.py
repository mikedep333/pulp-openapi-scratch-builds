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
from pulpcore.client.pulp_rpm.models.pulp_importer import PulpImporter  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestPulpImporter(unittest.TestCase):
    """PulpImporter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PulpImporter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.pulp_importer.PulpImporter()  # noqa: E501
        if include_optional :
            return PulpImporter(
                name = '0', 
                repo_mapping = {
                    'key' : '0'
                    }
            )
        else :
            return PulpImporter(
                name = '0',
        )

    def testPulpImporter(self):
        """Test PulpImporter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
