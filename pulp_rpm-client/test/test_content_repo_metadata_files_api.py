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
from pulpcore.client.pulp_rpm.api.content_repo_metadata_files_api import ContentRepoMetadataFilesApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestContentRepoMetadataFilesApi(unittest.TestCase):
    """ContentRepoMetadataFilesApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.content_repo_metadata_files_api.ContentRepoMetadataFilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_content_rpm_repo_metadata_files_list(self):
        """Test case for content_rpm_repo_metadata_files_list

        List repo metadata files  # noqa: E501
        """
        pass

    def test_content_rpm_repo_metadata_files_read(self):
        """Test case for content_rpm_repo_metadata_files_read

        Inspect a repo metadata file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
