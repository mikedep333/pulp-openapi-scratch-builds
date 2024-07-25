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
from pulpcore.client.pulp_rpm.api.repositories_file_api import RepositoriesFileApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestRepositoriesFileApi(unittest.TestCase):
    """RepositoriesFileApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.repositories_file_api.RepositoriesFileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_repositories_file_file_add_role(self):
        """Test case for repositories_file_file_add_role

        Add a role  # noqa: E501
        """
        pass

    def test_repositories_file_file_create(self):
        """Test case for repositories_file_file_create

        Create a file repository  # noqa: E501
        """
        pass

    def test_repositories_file_file_delete(self):
        """Test case for repositories_file_file_delete

        Delete a file repository  # noqa: E501
        """
        pass

    def test_repositories_file_file_list(self):
        """Test case for repositories_file_file_list

        List file repositorys  # noqa: E501
        """
        pass

    def test_repositories_file_file_list_roles(self):
        """Test case for repositories_file_file_list_roles

        List roles  # noqa: E501
        """
        pass

    def test_repositories_file_file_modify(self):
        """Test case for repositories_file_file_modify

        Modify Repository Content  # noqa: E501
        """
        pass

    def test_repositories_file_file_my_permissions(self):
        """Test case for repositories_file_file_my_permissions

        List user permissions  # noqa: E501
        """
        pass

    def test_repositories_file_file_partial_update(self):
        """Test case for repositories_file_file_partial_update

        Update a file repository  # noqa: E501
        """
        pass

    def test_repositories_file_file_read(self):
        """Test case for repositories_file_file_read

        Inspect a file repository  # noqa: E501
        """
        pass

    def test_repositories_file_file_remove_role(self):
        """Test case for repositories_file_file_remove_role

        Remove a role  # noqa: E501
        """
        pass

    def test_repositories_file_file_set_label(self):
        """Test case for repositories_file_file_set_label

        Set a label  # noqa: E501
        """
        pass

    def test_repositories_file_file_sync(self):
        """Test case for repositories_file_file_sync

        Sync from a remote  # noqa: E501
        """
        pass

    def test_repositories_file_file_unset_label(self):
        """Test case for repositories_file_file_unset_label

        Unset a label  # noqa: E501
        """
        pass

    def test_repositories_file_file_update(self):
        """Test case for repositories_file_file_update

        Update a file repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()