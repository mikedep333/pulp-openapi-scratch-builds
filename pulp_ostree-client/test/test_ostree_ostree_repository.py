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

import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.models.ostree_ostree_repository import OstreeOstreeRepository  # noqa: E501
from pulpcore.client.pulp_ostree.rest import ApiException

class TestOstreeOstreeRepository(unittest.TestCase):
    """OstreeOstreeRepository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OstreeOstreeRepository
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ostree.models.ostree_ostree_repository.OstreeOstreeRepository()  # noqa: E501
        if include_optional :
            return OstreeOstreeRepository(
                pulp_labels = {
                    'key' : '0'
                    }, 
                name = '0', 
                description = '0', 
                retain_repo_versions = 1, 
                remote = '0', 
                compute_delta = True
            )
        else :
            return OstreeOstreeRepository(
                name = '0',
        )

    def testOstreeOstreeRepository(self):
        """Test OstreeOstreeRepository"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()