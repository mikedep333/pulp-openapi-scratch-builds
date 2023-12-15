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


class VariantResponse(object):
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
        'variant_id': 'str',
        'uid': 'str',
        'name': 'str',
        'type': 'str',
        'packages': 'str',
        'source_packages': 'str',
        'source_repository': 'str',
        'debug_packages': 'str',
        'debug_repository': 'str',
        'identity': 'str'
    }

    attribute_map = {
        'variant_id': 'variant_id',
        'uid': 'uid',
        'name': 'name',
        'type': 'type',
        'packages': 'packages',
        'source_packages': 'source_packages',
        'source_repository': 'source_repository',
        'debug_packages': 'debug_packages',
        'debug_repository': 'debug_repository',
        'identity': 'identity'
    }

    def __init__(self, variant_id=None, uid=None, name=None, type=None, packages=None, source_packages=None, source_repository=None, debug_packages=None, debug_repository=None, identity=None, local_vars_configuration=None):  # noqa: E501
        """VariantResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._variant_id = None
        self._uid = None
        self._name = None
        self._type = None
        self._packages = None
        self._source_packages = None
        self._source_repository = None
        self._debug_packages = None
        self._debug_repository = None
        self._identity = None
        self.discriminator = None

        self.variant_id = variant_id
        self.uid = uid
        self.name = name
        self.type = type
        self.packages = packages
        self.source_packages = source_packages
        self.source_repository = source_repository
        self.debug_packages = debug_packages
        self.debug_repository = debug_repository
        self.identity = identity

    @property
    def variant_id(self):
        """Gets the variant_id of this VariantResponse.  # noqa: E501

        Variant id.  # noqa: E501

        :return: The variant_id of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._variant_id

    @variant_id.setter
    def variant_id(self, variant_id):
        """Sets the variant_id of this VariantResponse.

        Variant id.  # noqa: E501

        :param variant_id: The variant_id of this VariantResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and variant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `variant_id`, must not be `None`")  # noqa: E501

        self._variant_id = variant_id

    @property
    def uid(self):
        """Gets the uid of this VariantResponse.  # noqa: E501

        Variant uid.  # noqa: E501

        :return: The uid of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this VariantResponse.

        Variant uid.  # noqa: E501

        :param uid: The uid of this VariantResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this VariantResponse.  # noqa: E501

        Variant name.  # noqa: E501

        :return: The name of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariantResponse.

        Variant name.  # noqa: E501

        :param name: The name of this VariantResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this VariantResponse.  # noqa: E501

        Variant type.  # noqa: E501

        :return: The type of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariantResponse.

        Variant type.  # noqa: E501

        :param type: The type of this VariantResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def packages(self):
        """Gets the packages of this VariantResponse.  # noqa: E501

        Relative path to directory with binary RPMs.  # noqa: E501

        :return: The packages of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this VariantResponse.

        Relative path to directory with binary RPMs.  # noqa: E501

        :param packages: The packages of this VariantResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and packages is None:  # noqa: E501
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

    @property
    def source_packages(self):
        """Gets the source_packages of this VariantResponse.  # noqa: E501

        Relative path to directory with source RPMs.  # noqa: E501

        :return: The source_packages of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_packages

    @source_packages.setter
    def source_packages(self, source_packages):
        """Sets the source_packages of this VariantResponse.

        Relative path to directory with source RPMs.  # noqa: E501

        :param source_packages: The source_packages of this VariantResponse.  # noqa: E501
        :type: str
        """

        self._source_packages = source_packages

    @property
    def source_repository(self):
        """Gets the source_repository of this VariantResponse.  # noqa: E501

        Relative path to YUM repository with source RPMs.  # noqa: E501

        :return: The source_repository of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_repository

    @source_repository.setter
    def source_repository(self, source_repository):
        """Sets the source_repository of this VariantResponse.

        Relative path to YUM repository with source RPMs.  # noqa: E501

        :param source_repository: The source_repository of this VariantResponse.  # noqa: E501
        :type: str
        """

        self._source_repository = source_repository

    @property
    def debug_packages(self):
        """Gets the debug_packages of this VariantResponse.  # noqa: E501

        Relative path to directory with debug RPMs.  # noqa: E501

        :return: The debug_packages of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._debug_packages

    @debug_packages.setter
    def debug_packages(self, debug_packages):
        """Sets the debug_packages of this VariantResponse.

        Relative path to directory with debug RPMs.  # noqa: E501

        :param debug_packages: The debug_packages of this VariantResponse.  # noqa: E501
        :type: str
        """

        self._debug_packages = debug_packages

    @property
    def debug_repository(self):
        """Gets the debug_repository of this VariantResponse.  # noqa: E501

        Relative path to YUM repository with debug RPMs.  # noqa: E501

        :return: The debug_repository of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._debug_repository

    @debug_repository.setter
    def debug_repository(self, debug_repository):
        """Sets the debug_repository of this VariantResponse.

        Relative path to YUM repository with debug RPMs.  # noqa: E501

        :param debug_repository: The debug_repository of this VariantResponse.  # noqa: E501
        :type: str
        """

        self._debug_repository = debug_repository

    @property
    def identity(self):
        """Gets the identity of this VariantResponse.  # noqa: E501

        Relative path to a pem file that identifies a product.  # noqa: E501

        :return: The identity of this VariantResponse.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this VariantResponse.

        Relative path to a pem file that identifies a product.  # noqa: E501

        :param identity: The identity of this VariantResponse.  # noqa: E501
        :type: str
        """

        self._identity = identity

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
        if not isinstance(other, VariantResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VariantResponse):
            return True

        return self.to_dict() != other.to_dict()