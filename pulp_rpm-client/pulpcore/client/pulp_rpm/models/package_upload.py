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


class PackageUpload(object):
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
        'content': 'file',
        'action': 'str',
        'sha256_digest': 'str'
    }

    attribute_map = {
        'content': 'content',
        'action': 'action',
        'sha256_digest': 'sha256_digest'
    }

    def __init__(self, content=None, action='file_upload', sha256_digest=None, local_vars_configuration=None):  # noqa: E501
        """PackageUpload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._action = None
        self._sha256_digest = None
        self.discriminator = None

        self.content = content
        if action is not None:
            self.action = action
        self.sha256_digest = sha256_digest

    @property
    def content(self):
        """Gets the content of this PackageUpload.  # noqa: E501

        A Python package release file to upload to the index.  # noqa: E501

        :return: The content of this PackageUpload.  # noqa: E501
        :rtype: file
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PackageUpload.

        A Python package release file to upload to the index.  # noqa: E501

        :param content: The content of this PackageUpload.  # noqa: E501
        :type: file
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def action(self):
        """Gets the action of this PackageUpload.  # noqa: E501

        Defaults to `file_upload`, don't change it or request will fail!  # noqa: E501

        :return: The action of this PackageUpload.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PackageUpload.

        Defaults to `file_upload`, don't change it or request will fail!  # noqa: E501

        :param action: The action of this PackageUpload.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                action is not None and len(action) < 1):
            raise ValueError("Invalid value for `action`, length must be greater than or equal to `1`")  # noqa: E501

        self._action = action

    @property
    def sha256_digest(self):
        """Gets the sha256_digest of this PackageUpload.  # noqa: E501

        SHA256 of package to validate upload integrity.  # noqa: E501

        :return: The sha256_digest of this PackageUpload.  # noqa: E501
        :rtype: str
        """
        return self._sha256_digest

    @sha256_digest.setter
    def sha256_digest(self, sha256_digest):
        """Sets the sha256_digest of this PackageUpload.

        SHA256 of package to validate upload integrity.  # noqa: E501

        :param sha256_digest: The sha256_digest of this PackageUpload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sha256_digest is None:  # noqa: E501
            raise ValueError("Invalid value for `sha256_digest`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sha256_digest is not None and len(sha256_digest) > 64):
            raise ValueError("Invalid value for `sha256_digest`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sha256_digest is not None and len(sha256_digest) < 64):
            raise ValueError("Invalid value for `sha256_digest`, length must be greater than or equal to `64`")  # noqa: E501

        self._sha256_digest = sha256_digest

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
        if not isinstance(other, PackageUpload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageUpload):
            return True

        return self.to_dict() != other.to_dict()