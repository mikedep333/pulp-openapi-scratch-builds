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


class CertguardRHSMCertGuardResponse(object):
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
        'name': 'str',
        'description': 'str',
        'ca_certificate': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'name': 'name',
        'description': 'description',
        'ca_certificate': 'ca_certificate'
    }

    def __init__(self, pulp_href=None, pulp_created=None, pulp_last_updated=None, name=None, description=None, ca_certificate=None, local_vars_configuration=None):  # noqa: E501
        """CertguardRHSMCertGuardResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._name = None
        self._description = None
        self._ca_certificate = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        self.name = name
        self.description = description
        self.ca_certificate = ca_certificate

    @property
    def pulp_href(self):
        """Gets the pulp_href of this CertguardRHSMCertGuardResponse.  # noqa: E501


        :return: The pulp_href of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this CertguardRHSMCertGuardResponse.


        :param pulp_href: The pulp_href of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this CertguardRHSMCertGuardResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this CertguardRHSMCertGuardResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this CertguardRHSMCertGuardResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this CertguardRHSMCertGuardResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def name(self):
        """Gets the name of this CertguardRHSMCertGuardResponse.  # noqa: E501

        The unique name.  # noqa: E501

        :return: The name of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertguardRHSMCertGuardResponse.

        The unique name.  # noqa: E501

        :param name: The name of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CertguardRHSMCertGuardResponse.  # noqa: E501

        An optional description.  # noqa: E501

        :return: The description of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertguardRHSMCertGuardResponse.

        An optional description.  # noqa: E501

        :param description: The description of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ca_certificate(self):
        """Gets the ca_certificate of this CertguardRHSMCertGuardResponse.  # noqa: E501

        A Certificate Authority (CA) certificate (or a bundle thereof) used to verify client-certificate authenticity.  # noqa: E501

        :return: The ca_certificate of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """Sets the ca_certificate of this CertguardRHSMCertGuardResponse.

        A Certificate Authority (CA) certificate (or a bundle thereof) used to verify client-certificate authenticity.  # noqa: E501

        :param ca_certificate: The ca_certificate of this CertguardRHSMCertGuardResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ca_certificate is None:  # noqa: E501
            raise ValueError("Invalid value for `ca_certificate`, must not be `None`")  # noqa: E501

        self._ca_certificate = ca_certificate

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
        if not isinstance(other, CertguardRHSMCertGuardResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertguardRHSMCertGuardResponse):
            return True

        return self.to_dict() != other.to_dict()
