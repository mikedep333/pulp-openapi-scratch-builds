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
from pulpcore.client.pulp_rpm.api.task_groups_api import TaskGroupsApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestTaskGroupsApi(unittest.TestCase):
    """TaskGroupsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.task_groups_api.TaskGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_task_groups_list(self):
        """Test case for task_groups_list

        List task groups  # noqa: E501
        """
        pass

    def test_task_groups_read(self):
        """Test case for task_groups_read

        Inspect a task group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()