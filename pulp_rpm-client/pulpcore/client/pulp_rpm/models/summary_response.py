# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class SummaryResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'projects': 'int',
        'releases': 'int',
        'files': 'int'
    }

    attribute_map = {
        'projects': 'projects',
        'releases': 'releases',
        'files': 'files'
    }

    def __init__(self, projects=None, releases=None, files=None, local_vars_configuration=None):  # noqa: E501
        """SummaryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._projects = None
        self._releases = None
        self._files = None
        self.discriminator = None

        self.projects = projects
        self.releases = releases
        self.files = files

    @property
    def projects(self):
        """Gets the projects of this SummaryResponse.  # noqa: E501

        Number of Python projects in index  # noqa: E501

        :return: The projects of this SummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this SummaryResponse.

        Number of Python projects in index  # noqa: E501

        :param projects: The projects of this SummaryResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and projects is None:  # noqa: E501
            raise ValueError("Invalid value for `projects`, must not be `None`")  # noqa: E501

        self._projects = projects

    @property
    def releases(self):
        """Gets the releases of this SummaryResponse.  # noqa: E501

        Number of Python distribution releases in index  # noqa: E501

        :return: The releases of this SummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this SummaryResponse.

        Number of Python distribution releases in index  # noqa: E501

        :param releases: The releases of this SummaryResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and releases is None:  # noqa: E501
            raise ValueError("Invalid value for `releases`, must not be `None`")  # noqa: E501

        self._releases = releases

    @property
    def files(self):
        """Gets the files of this SummaryResponse.  # noqa: E501

        Number of files for all distributions in index  # noqa: E501

        :return: The files of this SummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this SummaryResponse.

        Number of files for all distributions in index  # noqa: E501

        :param files: The files of this SummaryResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and files is None:  # noqa: E501
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SummaryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SummaryResponse):
            return True

        return self.to_dict() != other.to_dict()
