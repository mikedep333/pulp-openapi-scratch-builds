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


class RpmUpdateRecord(object):
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
        'repository': 'str',
        'file': 'file',
        'upload': 'str'
    }

    attribute_map = {
        'repository': 'repository',
        'file': 'file',
        'upload': 'upload'
    }

    def __init__(self, repository=None, file=None, upload=None, local_vars_configuration=None):  # noqa: E501
        """RpmUpdateRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._repository = None
        self._file = None
        self._upload = None
        self.discriminator = None

        if repository is not None:
            self.repository = repository
        if file is not None:
            self.file = file
        if upload is not None:
            self.upload = upload

    @property
    def repository(self):
        """Gets the repository of this RpmUpdateRecord.  # noqa: E501

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :return: The repository of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RpmUpdateRecord.

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :param repository: The repository of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def file(self):
        """Gets the file of this RpmUpdateRecord.  # noqa: E501

        An uploaded file that may be turned into the content unit.  # noqa: E501

        :return: The file of this RpmUpdateRecord.  # noqa: E501
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this RpmUpdateRecord.

        An uploaded file that may be turned into the content unit.  # noqa: E501

        :param file: The file of this RpmUpdateRecord.  # noqa: E501
        :type: file
        """

        self._file = file

    @property
    def upload(self):
        """Gets the upload of this RpmUpdateRecord.  # noqa: E501

        An uncommitted upload that may be turned into the content unit.  # noqa: E501

        :return: The upload of this RpmUpdateRecord.  # noqa: E501
        :rtype: str
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this RpmUpdateRecord.

        An uncommitted upload that may be turned into the content unit.  # noqa: E501

        :param upload: The upload of this RpmUpdateRecord.  # noqa: E501
        :type: str
        """

        self._upload = upload

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
        if not isinstance(other, RpmUpdateRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmUpdateRecord):
            return True

        return self.to_dict() != other.to_dict()
