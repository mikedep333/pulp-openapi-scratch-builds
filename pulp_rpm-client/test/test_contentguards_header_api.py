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
from pulpcore.client.pulp_rpm.api.contentguards_header_api import ContentguardsHeaderApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestContentguardsHeaderApi(unittest.TestCase):
    """ContentguardsHeaderApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.contentguards_header_api.ContentguardsHeaderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_contentguards_core_header_add_role(self):
        """Test case for contentguards_core_header_add_role

        Add a role  # noqa: E501
        """
        pass

    def test_contentguards_core_header_create(self):
        """Test case for contentguards_core_header_create

        Create a header content guard  # noqa: E501
        """
        pass

    def test_contentguards_core_header_delete(self):
        """Test case for contentguards_core_header_delete

        Delete a header content guard  # noqa: E501
        """
        pass

    def test_contentguards_core_header_list(self):
        """Test case for contentguards_core_header_list

        List header content guards  # noqa: E501
        """
        pass

    def test_contentguards_core_header_list_roles(self):
        """Test case for contentguards_core_header_list_roles

        List roles  # noqa: E501
        """
        pass

    def test_contentguards_core_header_my_permissions(self):
        """Test case for contentguards_core_header_my_permissions

        List user permissions  # noqa: E501
        """
        pass

    def test_contentguards_core_header_partial_update(self):
        """Test case for contentguards_core_header_partial_update

        Update a header content guard  # noqa: E501
        """
        pass

    def test_contentguards_core_header_read(self):
        """Test case for contentguards_core_header_read

        Inspect a header content guard  # noqa: E501
        """
        pass

    def test_contentguards_core_header_remove_role(self):
        """Test case for contentguards_core_header_remove_role

        Remove a role  # noqa: E501
        """
        pass

    def test_contentguards_core_header_update(self):
        """Test case for contentguards_core_header_update

        Update a header content guard  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
