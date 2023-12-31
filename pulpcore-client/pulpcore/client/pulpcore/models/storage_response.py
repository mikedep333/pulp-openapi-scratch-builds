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


class StorageResponse(object):
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
        'total': 'int',
        'used': 'int',
        'free': 'int'
    }

    attribute_map = {
        'total': 'total',
        'used': 'used',
        'free': 'free'
    }

    def __init__(self, total=None, used=None, free=None, local_vars_configuration=None):  # noqa: E501
        """StorageResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._used = None
        self._free = None
        self.discriminator = None

        self.total = total
        self.used = used
        self.free = free

    @property
    def total(self):
        """Gets the total of this StorageResponse.  # noqa: E501

        Total number of bytes  # noqa: E501

        :return: The total of this StorageResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this StorageResponse.

        Total number of bytes  # noqa: E501

        :param total: The total of this StorageResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                total is not None and total < 0):  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

    @property
    def used(self):
        """Gets the used of this StorageResponse.  # noqa: E501

        Number of bytes in use  # noqa: E501

        :return: The used of this StorageResponse.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this StorageResponse.

        Number of bytes in use  # noqa: E501

        :param used: The used of this StorageResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                used is not None and used < 0):  # noqa: E501
            raise ValueError("Invalid value for `used`, must be a value greater than or equal to `0`")  # noqa: E501

        self._used = used

    @property
    def free(self):
        """Gets the free of this StorageResponse.  # noqa: E501

        Number of free bytes  # noqa: E501

        :return: The free of this StorageResponse.  # noqa: E501
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this StorageResponse.

        Number of free bytes  # noqa: E501

        :param free: The free of this StorageResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                free is not None and free < 0):  # noqa: E501
            raise ValueError("Invalid value for `free`, must be a value greater than or equal to `0`")  # noqa: E501

        self._free = free

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
        if not isinstance(other, StorageResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageResponse):
            return True

        return self.to_dict() != other.to_dict()
