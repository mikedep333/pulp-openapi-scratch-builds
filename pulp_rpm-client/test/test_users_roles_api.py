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

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.api.users_roles_api import UsersRolesApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestUsersRolesApi(unittest.TestCase):
    """UsersRolesApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.users_roles_api.UsersRolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_roles_create(self):
        """Test case for users_roles_create

        Create an user role  # noqa: E501
        """
        pass

    def test_users_roles_delete(self):
        """Test case for users_roles_delete

        Delete an user role  # noqa: E501
        """
        pass

    def test_users_roles_list(self):
        """Test case for users_roles_list

        List user roles  # noqa: E501
        """
        pass

    def test_users_roles_read(self):
        """Test case for users_roles_read

        Inspect an user role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()