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


class PublicationResponse(object):
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
        'pulp_last_updated': 'datetime',
        'repository_version': 'str',
        'repository': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'repository_version': 'repository_version',
        'repository': 'repository'
    }

    def __init__(self, pulp_href=None, pulp_created=None, pulp_last_updated=None, repository_version=None, repository=None, local_vars_configuration=None):  # noqa: E501
        """PublicationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._repository_version = None
        self._repository = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        if repository_version is not None:
            self.repository_version = repository_version
        if repository is not None:
            self.repository = repository

    @property
    def pulp_href(self):
        """Gets the pulp_href of this PublicationResponse.  # noqa: E501


        :return: The pulp_href of this PublicationResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this PublicationResponse.


        :param pulp_href: The pulp_href of this PublicationResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this PublicationResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this PublicationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this PublicationResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this PublicationResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this PublicationResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this PublicationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this PublicationResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this PublicationResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def repository_version(self):
        """Gets the repository_version of this PublicationResponse.  # noqa: E501


        :return: The repository_version of this PublicationResponse.  # noqa: E501
        :rtype: str
        """
        return self._repository_version

    @repository_version.setter
    def repository_version(self, repository_version):
        """Sets the repository_version of this PublicationResponse.


        :param repository_version: The repository_version of this PublicationResponse.  # noqa: E501
        :type: str
        """

        self._repository_version = repository_version

    @property
    def repository(self):
        """Gets the repository of this PublicationResponse.  # noqa: E501

        A URI of the repository to be published.  # noqa: E501

        :return: The repository of this PublicationResponse.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this PublicationResponse.

        A URI of the repository to be published.  # noqa: E501

        :param repository: The repository of this PublicationResponse.  # noqa: E501
        :type: str
        """

        self._repository = repository

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
        if not isinstance(other, PublicationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicationResponse):
            return True

        return self.to_dict() != other.to_dict()
