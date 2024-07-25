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
from pulpcore.client.pulp_rpm.models.paginatedgem_gem_content_response_list import PaginatedgemGemContentResponseList  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestPaginatedgemGemContentResponseList(unittest.TestCase):
    """PaginatedgemGemContentResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedgemGemContentResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.paginatedgem_gem_content_response_list.PaginatedgemGemContentResponseList()  # noqa: E501
        if include_optional :
            return PaginatedgemGemContentResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_rpm.models.gem/gem_content_response.gem.GemContentResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        artifacts = pulpcore.client.pulp_rpm.models.artifacts.artifacts(), 
                        checksum = '0', 
                        name = '0', 
                        version = '0', 
                        platform = '0', 
                        prerelease = True, 
                        dependencies = {
                            'key' : '0'
                            }, 
                        required_ruby_version = '0', 
                        required_rubygems_version = '0', )
                    ]
            )
        else :
            return PaginatedgemGemContentResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulp_rpm.models.gem/gem_content_response.gem.GemContentResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        artifacts = pulpcore.client.pulp_rpm.models.artifacts.artifacts(), 
                        checksum = '0', 
                        name = '0', 
                        version = '0', 
                        platform = '0', 
                        prerelease = True, 
                        dependencies = {
                            'key' : '0'
                            }, 
                        required_ruby_version = '0', 
                        required_rubygems_version = '0', )
                    ],
        )

    def testPaginatedgemGemContentResponseList(self):
        """Test PaginatedgemGemContentResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()