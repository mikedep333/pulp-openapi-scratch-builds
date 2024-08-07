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
from pulpcore.client.pulpcore.models.paginated_group_user_response_list import PaginatedGroupUserResponseList  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestPaginatedGroupUserResponseList(unittest.TestCase):
    """PaginatedGroupUserResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedGroupUserResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.paginated_group_user_response_list.PaginatedGroupUserResponseList()  # noqa: E501
        if include_optional :
            return PaginatedGroupUserResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulpcore.models.group_user_response.GroupUserResponse(
                        username = '0', 
                        pulp_href = '0', )
                    ]
            )
        else :
            return PaginatedGroupUserResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulpcore.models.group_user_response.GroupUserResponse(
                        username = '0', 
                        pulp_href = '0', )
                    ],
        )

    def testPaginatedGroupUserResponseList(self):
        """Test PaginatedGroupUserResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
