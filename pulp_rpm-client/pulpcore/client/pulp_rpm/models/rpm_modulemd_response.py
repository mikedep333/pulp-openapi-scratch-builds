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


class RpmModulemdResponse(object):
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
        'stream': 'str',
        'version': 'str',
        'static_context': 'bool',
        'context': 'str',
        'arch': 'str',
        'artifacts': 'object',
        'dependencies': 'object',
        'packages': 'list[str]',
        'profiles': 'object',
        'description': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'name': 'name',
        'stream': 'stream',
        'version': 'version',
        'static_context': 'static_context',
        'context': 'context',
        'arch': 'arch',
        'artifacts': 'artifacts',
        'dependencies': 'dependencies',
        'packages': 'packages',
        'profiles': 'profiles',
        'description': 'description'
    }

    def __init__(self, pulp_href=None, pulp_created=None, pulp_last_updated=None, name=None, stream=None, version=None, static_context=None, context=None, arch=None, artifacts=None, dependencies=None, packages=None, profiles=None, description=None, local_vars_configuration=None):  # noqa: E501
        """RpmModulemdResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._name = None
        self._stream = None
        self._version = None
        self._static_context = None
        self._context = None
        self._arch = None
        self._artifacts = None
        self._dependencies = None
        self._packages = None
        self._profiles = None
        self._description = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        self.name = name
        self.stream = stream
        self.version = version
        if static_context is not None:
            self.static_context = static_context
        self.context = context
        self.arch = arch
        self.artifacts = artifacts
        self.dependencies = dependencies
        if packages is not None:
            self.packages = packages
        self.profiles = profiles
        self.description = description

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RpmModulemdResponse.  # noqa: E501


        :return: The pulp_href of this RpmModulemdResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RpmModulemdResponse.


        :param pulp_href: The pulp_href of this RpmModulemdResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RpmModulemdResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RpmModulemdResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RpmModulemdResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RpmModulemdResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this RpmModulemdResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this RpmModulemdResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this RpmModulemdResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this RpmModulemdResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def name(self):
        """Gets the name of this RpmModulemdResponse.  # noqa: E501

        Modulemd name.  # noqa: E501

        :return: The name of this RpmModulemdResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RpmModulemdResponse.

        Modulemd name.  # noqa: E501

        :param name: The name of this RpmModulemdResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def stream(self):
        """Gets the stream of this RpmModulemdResponse.  # noqa: E501

        Stream name.  # noqa: E501

        :return: The stream of this RpmModulemdResponse.  # noqa: E501
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this RpmModulemdResponse.

        Stream name.  # noqa: E501

        :param stream: The stream of this RpmModulemdResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and stream is None:  # noqa: E501
            raise ValueError("Invalid value for `stream`, must not be `None`")  # noqa: E501

        self._stream = stream

    @property
    def version(self):
        """Gets the version of this RpmModulemdResponse.  # noqa: E501

        Modulemd version.  # noqa: E501

        :return: The version of this RpmModulemdResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RpmModulemdResponse.

        Modulemd version.  # noqa: E501

        :param version: The version of this RpmModulemdResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def static_context(self):
        """Gets the static_context of this RpmModulemdResponse.  # noqa: E501

        Modulemd static-context flag.  # noqa: E501

        :return: The static_context of this RpmModulemdResponse.  # noqa: E501
        :rtype: bool
        """
        return self._static_context

    @static_context.setter
    def static_context(self, static_context):
        """Sets the static_context of this RpmModulemdResponse.

        Modulemd static-context flag.  # noqa: E501

        :param static_context: The static_context of this RpmModulemdResponse.  # noqa: E501
        :type: bool
        """

        self._static_context = static_context

    @property
    def context(self):
        """Gets the context of this RpmModulemdResponse.  # noqa: E501

        Modulemd context.  # noqa: E501

        :return: The context of this RpmModulemdResponse.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this RpmModulemdResponse.

        Modulemd context.  # noqa: E501

        :param context: The context of this RpmModulemdResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and context is None:  # noqa: E501
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def arch(self):
        """Gets the arch of this RpmModulemdResponse.  # noqa: E501

        Modulemd architecture.  # noqa: E501

        :return: The arch of this RpmModulemdResponse.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this RpmModulemdResponse.

        Modulemd architecture.  # noqa: E501

        :param arch: The arch of this RpmModulemdResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and arch is None:  # noqa: E501
            raise ValueError("Invalid value for `arch`, must not be `None`")  # noqa: E501

        self._arch = arch

    @property
    def artifacts(self):
        """Gets the artifacts of this RpmModulemdResponse.  # noqa: E501

        Modulemd artifacts.  # noqa: E501

        :return: The artifacts of this RpmModulemdResponse.  # noqa: E501
        :rtype: object
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this RpmModulemdResponse.

        Modulemd artifacts.  # noqa: E501

        :param artifacts: The artifacts of this RpmModulemdResponse.  # noqa: E501
        :type: object
        """

        self._artifacts = artifacts

    @property
    def dependencies(self):
        """Gets the dependencies of this RpmModulemdResponse.  # noqa: E501

        Modulemd dependencies.  # noqa: E501

        :return: The dependencies of this RpmModulemdResponse.  # noqa: E501
        :rtype: object
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this RpmModulemdResponse.

        Modulemd dependencies.  # noqa: E501

        :param dependencies: The dependencies of this RpmModulemdResponse.  # noqa: E501
        :type: object
        """

        self._dependencies = dependencies

    @property
    def packages(self):
        """Gets the packages of this RpmModulemdResponse.  # noqa: E501

        Modulemd artifacts' packages.  # noqa: E501

        :return: The packages of this RpmModulemdResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this RpmModulemdResponse.

        Modulemd artifacts' packages.  # noqa: E501

        :param packages: The packages of this RpmModulemdResponse.  # noqa: E501
        :type: list[str]
        """

        self._packages = packages

    @property
    def profiles(self):
        """Gets the profiles of this RpmModulemdResponse.  # noqa: E501

        Modulemd profiles.  # noqa: E501

        :return: The profiles of this RpmModulemdResponse.  # noqa: E501
        :rtype: object
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this RpmModulemdResponse.

        Modulemd profiles.  # noqa: E501

        :param profiles: The profiles of this RpmModulemdResponse.  # noqa: E501
        :type: object
        """

        self._profiles = profiles

    @property
    def description(self):
        """Gets the description of this RpmModulemdResponse.  # noqa: E501

        Description of module.  # noqa: E501

        :return: The description of this RpmModulemdResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RpmModulemdResponse.

        Description of module.  # noqa: E501

        :param description: The description of this RpmModulemdResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, RpmModulemdResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmModulemdResponse):
            return True

        return self.to_dict() != other.to_dict()
