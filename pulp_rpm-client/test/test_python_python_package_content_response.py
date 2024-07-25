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

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.python_python_package_content_response import PythonPythonPackageContentResponse  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestPythonPythonPackageContentResponse(unittest.TestCase):
    """PythonPythonPackageContentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PythonPythonPackageContentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.python_python_package_content_response.PythonPythonPackageContentResponse()  # noqa: E501
        if include_optional :
            return PythonPythonPackageContentResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                artifact = '0', 
                filename = '0', 
                packagetype = '0', 
                name = '0', 
                version = '0', 
                sha256 = '0', 
                metadata_version = '0', 
                summary = '0', 
                description = '0', 
                description_content_type = '0', 
                keywords = '0', 
                home_page = '0', 
                download_url = '0', 
                author = '0', 
                author_email = '0', 
                maintainer = '0', 
                maintainer_email = '0', 
                license = '0', 
                requires_python = '0', 
                project_url = '0', 
                project_urls = null, 
                platform = '0', 
                supported_platform = '0', 
                requires_dist = null, 
                provides_dist = null, 
                obsoletes_dist = null, 
                requires_external = null, 
                classifiers = null
            )
        else :
            return PythonPythonPackageContentResponse(
        )

    def testPythonPythonPackageContentResponse(self):
        """Test PythonPythonPackageContentResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
