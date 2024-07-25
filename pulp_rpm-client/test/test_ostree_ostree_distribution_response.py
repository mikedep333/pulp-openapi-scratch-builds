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
from pulpcore.client.pulp_rpm.models.ostree_ostree_distribution_response import OstreeOstreeDistributionResponse  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestOstreeOstreeDistributionResponse(unittest.TestCase):
    """OstreeOstreeDistributionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OstreeOstreeDistributionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.ostree_ostree_distribution_response.OstreeOstreeDistributionResponse()  # noqa: E501
        if include_optional :
            return OstreeOstreeDistributionResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                base_path = '0', 
                base_url = '0', 
                content_guard = '0', 
                hidden = True, 
                pulp_labels = {
                    'key' : '0'
                    }, 
                name = '0', 
                repository = '0', 
                repository_version = '0'
            )
        else :
            return OstreeOstreeDistributionResponse(
                base_path = '0',
                name = '0',
        )

    def testOstreeOstreeDistributionResponse(self):
        """Test OstreeOstreeDistributionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()