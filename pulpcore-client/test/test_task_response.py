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
import datetime

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.task_response import TaskResponse  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestTaskResponse(unittest.TestCase):
    """TaskResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.task_response.TaskResponse()  # noqa: E501
        if include_optional :
            return TaskResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                state = '0', 
                name = '0', 
                logging_cid = '0', 
                created_by = '0', 
                unblocked_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                error = {
                    'key' : null
                    }, 
                worker = '0', 
                parent_task = '0', 
                child_tasks = [
                    '0'
                    ], 
                task_group = '0', 
                progress_reports = [
                    pulpcore.client.pulpcore.models.progress_report_response.ProgressReportResponse(
                        message = '0', 
                        code = '0', 
                        state = '0', 
                        total = 56, 
                        done = 56, 
                        suffix = '0', )
                    ], 
                created_resources = [
                    '0'
                    ], 
                reserved_resources_record = [
                    '0'
                    ]
            )
        else :
            return TaskResponse(
                name = '0',
                logging_cid = '0',
        )

    def testTaskResponse(self):
        """Test TaskResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
