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


class ContentSettingsResponse(object):
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
        'content_origin': 'str',
        'content_path_prefix': 'str'
    }

    attribute_map = {
        'content_origin': 'content_origin',
        'content_path_prefix': 'content_path_prefix'
    }

    def __init__(self, content_origin=None, content_path_prefix=None, local_vars_configuration=None):  # noqa: E501
        """ContentSettingsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content_origin = None
        self._content_path_prefix = None
        self.discriminator = None

        self.content_origin = content_origin
        self.content_path_prefix = content_path_prefix

    @property
    def content_origin(self):
        """Gets the content_origin of this ContentSettingsResponse.  # noqa: E501

        The CONTENT_ORIGIN setting for this Pulp instance  # noqa: E501

        :return: The content_origin of this ContentSettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_origin

    @content_origin.setter
    def content_origin(self, content_origin):
        """Sets the content_origin of this ContentSettingsResponse.

        The CONTENT_ORIGIN setting for this Pulp instance  # noqa: E501

        :param content_origin: The content_origin of this ContentSettingsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and content_origin is None:  # noqa: E501
            raise ValueError("Invalid value for `content_origin`, must not be `None`")  # noqa: E501

        self._content_origin = content_origin

    @property
    def content_path_prefix(self):
        """Gets the content_path_prefix of this ContentSettingsResponse.  # noqa: E501

        The CONTENT_PATH_PREFIX setting for this Pulp instance  # noqa: E501

        :return: The content_path_prefix of this ContentSettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_path_prefix

    @content_path_prefix.setter
    def content_path_prefix(self, content_path_prefix):
        """Sets the content_path_prefix of this ContentSettingsResponse.

        The CONTENT_PATH_PREFIX setting for this Pulp instance  # noqa: E501

        :param content_path_prefix: The content_path_prefix of this ContentSettingsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and content_path_prefix is None:  # noqa: E501
            raise ValueError("Invalid value for `content_path_prefix`, must not be `None`")  # noqa: E501

        self._content_path_prefix = content_path_prefix

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
        if not isinstance(other, ContentSettingsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentSettingsResponse):
            return True

        return self.to_dict() != other.to_dict()