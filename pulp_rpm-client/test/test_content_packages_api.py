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
from pulpcore.client.pulp_rpm.api.content_packages_api import ContentPackagesApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestContentPackagesApi(unittest.TestCase):
    """ContentPackagesApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.content_packages_api.ContentPackagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_content_rpm_packages_create(self):
        """Test case for content_rpm_packages_create

        Create a package  # noqa: E501
        """
        pass

    def test_content_rpm_packages_list(self):
        """Test case for content_rpm_packages_list

        List packages  # noqa: E501
        """
        pass

    def test_content_rpm_packages_read(self):
        """Test case for content_rpm_packages_read

        Inspect a package  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
