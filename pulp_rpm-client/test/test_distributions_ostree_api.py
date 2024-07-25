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
from pulpcore.client.pulp_rpm.api.distributions_ostree_api import DistributionsOstreeApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestDistributionsOstreeApi(unittest.TestCase):
    """DistributionsOstreeApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.distributions_ostree_api.DistributionsOstreeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_distributions_ostree_ostree_add_role(self):
        """Test case for distributions_ostree_ostree_add_role

        Add a role  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_create(self):
        """Test case for distributions_ostree_ostree_create

        Create an ostree distribution  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_delete(self):
        """Test case for distributions_ostree_ostree_delete

        Delete an ostree distribution  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_list(self):
        """Test case for distributions_ostree_ostree_list

        List ostree distributions  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_list_roles(self):
        """Test case for distributions_ostree_ostree_list_roles

        List roles  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_my_permissions(self):
        """Test case for distributions_ostree_ostree_my_permissions

        List user permissions  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_partial_update(self):
        """Test case for distributions_ostree_ostree_partial_update

        Update an ostree distribution  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_read(self):
        """Test case for distributions_ostree_ostree_read

        Inspect an ostree distribution  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_remove_role(self):
        """Test case for distributions_ostree_ostree_remove_role

        Remove a role  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_set_label(self):
        """Test case for distributions_ostree_ostree_set_label

        Set a label  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_unset_label(self):
        """Test case for distributions_ostree_ostree_unset_label

        Unset a label  # noqa: E501
        """
        pass

    def test_distributions_ostree_ostree_update(self):
        """Test case for distributions_ostree_ostree_update

        Update an ostree distribution  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()