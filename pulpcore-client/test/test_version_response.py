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

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.version_response import VersionResponse  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestVersionResponse(unittest.TestCase):
    """VersionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VersionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.version_response.VersionResponse()  # noqa: E501
        if include_optional :
            return VersionResponse(
                component = '0', 
                version = '0', 
                package = '0', 
                module = '0', 
                domain_compatible = True
            )
        else :
            return VersionResponse(
                component = '0',
                version = '0',
                package = '0',
                module = '0',
                domain_compatible = True,
        )

    def testVersionResponse(self):
        """Test VersionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
