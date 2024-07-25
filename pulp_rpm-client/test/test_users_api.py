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
from pulpcore.client.pulp_rpm.api.users_api import UsersApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_create(self):
        """Test case for users_create

        Create an user  # noqa: E501
        """
        pass

    def test_users_delete(self):
        """Test case for users_delete

        Delete an user  # noqa: E501
        """
        pass

    def test_users_list(self):
        """Test case for users_list

        List users  # noqa: E501
        """
        pass

    def test_users_partial_update(self):
        """Test case for users_partial_update

        Update an user  # noqa: E501
        """
        pass

    def test_users_read(self):
        """Test case for users_read

        Inspect an user  # noqa: E501
        """
        pass

    def test_users_update(self):
        """Test case for users_update

        Update an user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
