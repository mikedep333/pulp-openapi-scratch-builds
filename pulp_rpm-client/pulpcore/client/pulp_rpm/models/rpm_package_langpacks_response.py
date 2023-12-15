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


class RpmPackageLangpacksResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'matches': 'object',
        'digest': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'matches': 'matches',
        'digest': 'digest'
    }

    def __init__(self, pulp_href=None, pulp_created=None, matches=None, digest=None, local_vars_configuration=None):  # noqa: E501
        """RpmPackageLangpacksResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._matches = None
        self._digest = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.matches = matches
        self.digest = digest

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RpmPackageLangpacksResponse.  # noqa: E501


        :return: The pulp_href of this RpmPackageLangpacksResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RpmPackageLangpacksResponse.


        :param pulp_href: The pulp_href of this RpmPackageLangpacksResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RpmPackageLangpacksResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RpmPackageLangpacksResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RpmPackageLangpacksResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RpmPackageLangpacksResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def matches(self):
        """Gets the matches of this RpmPackageLangpacksResponse.  # noqa: E501

        Langpacks matches.  # noqa: E501

        :return: The matches of this RpmPackageLangpacksResponse.  # noqa: E501
        :rtype: object
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this RpmPackageLangpacksResponse.

        Langpacks matches.  # noqa: E501

        :param matches: The matches of this RpmPackageLangpacksResponse.  # noqa: E501
        :type: object
        """

        self._matches = matches

    @property
    def digest(self):
        """Gets the digest of this RpmPackageLangpacksResponse.  # noqa: E501

        Langpacks digest.  # noqa: E501

        :return: The digest of this RpmPackageLangpacksResponse.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this RpmPackageLangpacksResponse.

        Langpacks digest.  # noqa: E501

        :param digest: The digest of this RpmPackageLangpacksResponse.  # noqa: E501
        :type: str
        """

        self._digest = digest

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
        if not isinstance(other, RpmPackageLangpacksResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmPackageLangpacksResponse):
            return True

        return self.to_dict() != other.to_dict()