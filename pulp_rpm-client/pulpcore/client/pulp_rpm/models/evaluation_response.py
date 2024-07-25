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


class EvaluationResponse(object):
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
        'context': 'str',
        'is_valid': 'bool',
        'messages': 'list[str]'
    }

    attribute_map = {
        'context': 'context',
        'is_valid': 'is_valid',
        'messages': 'messages'
    }

    def __init__(self, context=None, is_valid=None, messages=None, local_vars_configuration=None):  # noqa: E501
        """EvaluationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._context = None
        self._is_valid = None
        self._messages = None
        self.discriminator = None

        self.context = context
        self.is_valid = is_valid
        self.messages = messages

    @property
    def context(self):
        """Gets the context of this EvaluationResponse.  # noqa: E501

        Parameter value being evaluated.  # noqa: E501

        :return: The context of this EvaluationResponse.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this EvaluationResponse.

        Parameter value being evaluated.  # noqa: E501

        :param context: The context of this EvaluationResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and context is None:  # noqa: E501
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def is_valid(self):
        """Gets the is_valid of this EvaluationResponse.  # noqa: E501

        True if evaluation passed, false otherwise.  # noqa: E501

        :return: The is_valid of this EvaluationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this EvaluationResponse.

        True if evaluation passed, false otherwise.  # noqa: E501

        :param is_valid: The is_valid of this EvaluationResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_valid is None:  # noqa: E501
            raise ValueError("Invalid value for `is_valid`, must not be `None`")  # noqa: E501

        self._is_valid = is_valid

    @property
    def messages(self):
        """Gets the messages of this EvaluationResponse.  # noqa: E501

        Messages describing results of all evaluations done. May be an empty list.  # noqa: E501

        :return: The messages of this EvaluationResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this EvaluationResponse.

        Messages describing results of all evaluations done. May be an empty list.  # noqa: E501

        :param messages: The messages of this EvaluationResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and messages is None:  # noqa: E501
            raise ValueError("Invalid value for `messages`, must not be `None`")  # noqa: E501

        self._messages = messages

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
        if not isinstance(other, EvaluationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EvaluationResponse):
            return True

        return self.to_dict() != other.to_dict()
