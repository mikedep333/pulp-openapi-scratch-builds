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
from pulpcore.client.pulp_rpm.api.roles_api import RolesApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_roles_create(self):
        """Test case for roles_create

        Create a role  # noqa: E501
        """
        pass

    def test_roles_delete(self):
        """Test case for roles_delete

        Delete a role  # noqa: E501
        """
        pass

    def test_roles_list(self):
        """Test case for roles_list

        List roles  # noqa: E501
        """
        pass

    def test_roles_partial_update(self):
        """Test case for roles_partial_update

        Update a role  # noqa: E501
        """
        pass

    def test_roles_read(self):
        """Test case for roles_read

        Inspect a role  # noqa: E501
        """
        pass

    def test_roles_update(self):
        """Test case for roles_update

        Update a role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()