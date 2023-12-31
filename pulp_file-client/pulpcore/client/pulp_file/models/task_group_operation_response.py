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

from pulpcore.client.pulp_file.configuration import Configuration


class TaskGroupOperationResponse(object):
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
        'task_group': 'str'
    }

    attribute_map = {
        'task_group': 'task_group'
    }

    def __init__(self, task_group=None, local_vars_configuration=None):  # noqa: E501
        """TaskGroupOperationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._task_group = None
        self.discriminator = None

        self.task_group = task_group

    @property
    def task_group(self):
        """Gets the task_group of this TaskGroupOperationResponse.  # noqa: E501

        The href of the task group.  # noqa: E501

        :return: The task_group of this TaskGroupOperationResponse.  # noqa: E501
        :rtype: str
        """
        return self._task_group

    @task_group.setter
    def task_group(self, task_group):
        """Sets the task_group of this TaskGroupOperationResponse.

        The href of the task group.  # noqa: E501

        :param task_group: The task_group of this TaskGroupOperationResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and task_group is None:  # noqa: E501
            raise ValueError("Invalid value for `task_group`, must not be `None`")  # noqa: E501

        self._task_group = task_group

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
        if not isinstance(other, TaskGroupOperationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskGroupOperationResponse):
            return True

        return self.to_dict() != other.to_dict()
