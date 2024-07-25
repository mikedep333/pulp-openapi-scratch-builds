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
from pulpcore.client.pulp_rpm.api.groups_users_api import GroupsUsersApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestGroupsUsersApi(unittest.TestCase):
    """GroupsUsersApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.groups_users_api.GroupsUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_groups_users_create(self):
        """Test case for groups_users_create

        Create an user  # noqa: E501
        """
        pass

    def test_groups_users_delete(self):
        """Test case for groups_users_delete

        Delete an user  # noqa: E501
        """
        pass

    def test_groups_users_list(self):
        """Test case for groups_users_list

        List users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
