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

from pulpcore.client.pulpcore.configuration import Configuration


class ContentAppStatusResponse(object):
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
        'name': 'str',
        'last_heartbeat': 'datetime',
        'versions': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'last_heartbeat': 'last_heartbeat',
        'versions': 'versions'
    }

    def __init__(self, name=None, last_heartbeat=None, versions=None, local_vars_configuration=None):  # noqa: E501
        """ContentAppStatusResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._last_heartbeat = None
        self._versions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if last_heartbeat is not None:
            self.last_heartbeat = last_heartbeat
        if versions is not None:
            self.versions = versions

    @property
    def name(self):
        """Gets the name of this ContentAppStatusResponse.  # noqa: E501

        The name of the worker.  # noqa: E501

        :return: The name of this ContentAppStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentAppStatusResponse.

        The name of the worker.  # noqa: E501

        :param name: The name of this ContentAppStatusResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def last_heartbeat(self):
        """Gets the last_heartbeat of this ContentAppStatusResponse.  # noqa: E501

        Timestamp of the last time the worker talked to the service.  # noqa: E501

        :return: The last_heartbeat of this ContentAppStatusResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_heartbeat

    @last_heartbeat.setter
    def last_heartbeat(self, last_heartbeat):
        """Sets the last_heartbeat of this ContentAppStatusResponse.

        Timestamp of the last time the worker talked to the service.  # noqa: E501

        :param last_heartbeat: The last_heartbeat of this ContentAppStatusResponse.  # noqa: E501
        :type: datetime
        """

        self._last_heartbeat = last_heartbeat

    @property
    def versions(self):
        """Gets the versions of this ContentAppStatusResponse.  # noqa: E501

        Versions of the components installed.  # noqa: E501

        :return: The versions of this ContentAppStatusResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ContentAppStatusResponse.

        Versions of the components installed.  # noqa: E501

        :param versions: The versions of this ContentAppStatusResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._versions = versions

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
        if not isinstance(other, ContentAppStatusResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentAppStatusResponse):
            return True

        return self.to_dict() != other.to_dict()
