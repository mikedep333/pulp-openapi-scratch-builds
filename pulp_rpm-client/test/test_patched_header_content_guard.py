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
from pulpcore.client.pulp_rpm.models.patched_header_content_guard import PatchedHeaderContentGuard  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestPatchedHeaderContentGuard(unittest.TestCase):
    """PatchedHeaderContentGuard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedHeaderContentGuard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.patched_header_content_guard.PatchedHeaderContentGuard()  # noqa: E501
        if include_optional :
            return PatchedHeaderContentGuard(
                name = '0', 
                description = '0', 
                header_name = '0', 
                header_value = '0', 
                jq_filter = '0'
            )
        else :
            return PatchedHeaderContentGuard(
        )

    def testPatchedHeaderContentGuard(self):
        """Test PatchedHeaderContentGuard"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
