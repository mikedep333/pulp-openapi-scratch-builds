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
from pulpcore.client.pulpcore.models.upstream_pulp import UpstreamPulp  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestUpstreamPulp(unittest.TestCase):
    """UpstreamPulp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpstreamPulp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.upstream_pulp.UpstreamPulp()  # noqa: E501
        if include_optional :
            return UpstreamPulp(
                name = '0', 
                base_url = '0', 
                api_root = '0', 
                domain = '0', 
                ca_cert = '0', 
                client_cert = '0', 
                client_key = '0', 
                tls_validation = True, 
                username = '0', 
                password = '0', 
                pulp_label_select = '0'
            )
        else :
            return UpstreamPulp(
                name = '0',
                base_url = '0',
                api_root = '0',
        )

    def testUpstreamPulp(self):
        """Test UpstreamPulp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
