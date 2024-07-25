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
from pulpcore.client.pulp_rpm.models.paginated_role_response_list import PaginatedRoleResponseList  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestPaginatedRoleResponseList(unittest.TestCase):
    """PaginatedRoleResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedRoleResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.paginated_role_response_list.PaginatedRoleResponseList()  # noqa: E501
        if include_optional :
            return PaginatedRoleResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_rpm.models.role_response.RoleResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        description = '0', 
                        permissions = [
                            '0'
                            ], 
                        locked = True, )
                    ]
            )
        else :
            return PaginatedRoleResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulp_rpm.models.role_response.RoleResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        description = '0', 
                        permissions = [
                            '0'
                            ], 
                        locked = True, )
                    ],
        )

    def testPaginatedRoleResponseList(self):
        """Test PaginatedRoleResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
