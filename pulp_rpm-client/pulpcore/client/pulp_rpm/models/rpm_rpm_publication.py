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


class RpmRpmPublication(object):
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
        'repository_version': 'str',
        'repository': 'str',
        'checksum_type': 'PackageChecksumTypeEnum',
        'metadata_checksum_type': 'PackageChecksumTypeEnum',
        'package_checksum_type': 'PackageChecksumTypeEnum',
        'gpgcheck': 'int',
        'repo_gpgcheck': 'int',
        'repo_config': 'object',
        'compression_type': 'CompressionTypeEnum'
    }

    attribute_map = {
        'repository_version': 'repository_version',
        'repository': 'repository',
        'checksum_type': 'checksum_type',
        'metadata_checksum_type': 'metadata_checksum_type',
        'package_checksum_type': 'package_checksum_type',
        'gpgcheck': 'gpgcheck',
        'repo_gpgcheck': 'repo_gpgcheck',
        'repo_config': 'repo_config',
        'compression_type': 'compression_type'
    }

    def __init__(self, repository_version=None, repository=None, checksum_type=None, metadata_checksum_type=None, package_checksum_type=None, gpgcheck=None, repo_gpgcheck=None, repo_config=None, compression_type=None, local_vars_configuration=None):  # noqa: E501
        """RpmRpmPublication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._repository_version = None
        self._repository = None
        self._checksum_type = None
        self._metadata_checksum_type = None
        self._package_checksum_type = None
        self._gpgcheck = None
        self._repo_gpgcheck = None
        self._repo_config = None
        self._compression_type = None
        self.discriminator = None

        if repository_version is not None:
            self.repository_version = repository_version
        if repository is not None:
            self.repository = repository
        if checksum_type is not None:
            self.checksum_type = checksum_type
        if metadata_checksum_type is not None:
            self.metadata_checksum_type = metadata_checksum_type
        if package_checksum_type is not None:
            self.package_checksum_type = package_checksum_type
        self.gpgcheck = gpgcheck
        self.repo_gpgcheck = repo_gpgcheck
        if repo_config is not None:
            self.repo_config = repo_config
        if compression_type is not None:
            self.compression_type = compression_type

    @property
    def repository_version(self):
        """Gets the repository_version of this RpmRpmPublication.  # noqa: E501


        :return: The repository_version of this RpmRpmPublication.  # noqa: E501
        :rtype: str
        """
        return self._repository_version

    @repository_version.setter
    def repository_version(self, repository_version):
        """Sets the repository_version of this RpmRpmPublication.


        :param repository_version: The repository_version of this RpmRpmPublication.  # noqa: E501
        :type: str
        """

        self._repository_version = repository_version

    @property
    def repository(self):
        """Gets the repository of this RpmRpmPublication.  # noqa: E501

        A URI of the repository to be published.  # noqa: E501

        :return: The repository of this RpmRpmPublication.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RpmRpmPublication.

        A URI of the repository to be published.  # noqa: E501

        :param repository: The repository of this RpmRpmPublication.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def checksum_type(self):
        """Gets the checksum_type of this RpmRpmPublication.  # noqa: E501

        The preferred checksum type used during repo publishes.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :return: The checksum_type of this RpmRpmPublication.  # noqa: E501
        :rtype: PackageChecksumTypeEnum
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """Sets the checksum_type of this RpmRpmPublication.

        The preferred checksum type used during repo publishes.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :param checksum_type: The checksum_type of this RpmRpmPublication.  # noqa: E501
        :type: PackageChecksumTypeEnum
        """

        self._checksum_type = checksum_type

    @property
    def metadata_checksum_type(self):
        """Gets the metadata_checksum_type of this RpmRpmPublication.  # noqa: E501

        DEPRECATED: The checksum type for metadata.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :return: The metadata_checksum_type of this RpmRpmPublication.  # noqa: E501
        :rtype: PackageChecksumTypeEnum
        """
        return self._metadata_checksum_type

    @metadata_checksum_type.setter
    def metadata_checksum_type(self, metadata_checksum_type):
        """Sets the metadata_checksum_type of this RpmRpmPublication.

        DEPRECATED: The checksum type for metadata.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :param metadata_checksum_type: The metadata_checksum_type of this RpmRpmPublication.  # noqa: E501
        :type: PackageChecksumTypeEnum
        """

        self._metadata_checksum_type = metadata_checksum_type

    @property
    def package_checksum_type(self):
        """Gets the package_checksum_type of this RpmRpmPublication.  # noqa: E501

        DEPRECATED: The checksum type for packages.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :return: The package_checksum_type of this RpmRpmPublication.  # noqa: E501
        :rtype: PackageChecksumTypeEnum
        """
        return self._package_checksum_type

    @package_checksum_type.setter
    def package_checksum_type(self, package_checksum_type):
        """Sets the package_checksum_type of this RpmRpmPublication.

        DEPRECATED: The checksum type for packages.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :param package_checksum_type: The package_checksum_type of this RpmRpmPublication.  # noqa: E501
        :type: PackageChecksumTypeEnum
        """

        self._package_checksum_type = package_checksum_type

    @property
    def gpgcheck(self):
        """Gets the gpgcheck of this RpmRpmPublication.  # noqa: E501

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages.  # noqa: E501

        :return: The gpgcheck of this RpmRpmPublication.  # noqa: E501
        :rtype: int
        """
        return self._gpgcheck

    @gpgcheck.setter
    def gpgcheck(self, gpgcheck):
        """Sets the gpgcheck of this RpmRpmPublication.

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages.  # noqa: E501

        :param gpgcheck: The gpgcheck of this RpmRpmPublication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gpgcheck is not None and gpgcheck > 1):  # noqa: E501
            raise ValueError("Invalid value for `gpgcheck`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                gpgcheck is not None and gpgcheck < 0):  # noqa: E501
            raise ValueError("Invalid value for `gpgcheck`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gpgcheck = gpgcheck

    @property
    def repo_gpgcheck(self):
        """Gets the repo_gpgcheck of this RpmRpmPublication.  # noqa: E501

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata.  # noqa: E501

        :return: The repo_gpgcheck of this RpmRpmPublication.  # noqa: E501
        :rtype: int
        """
        return self._repo_gpgcheck

    @repo_gpgcheck.setter
    def repo_gpgcheck(self, repo_gpgcheck):
        """Sets the repo_gpgcheck of this RpmRpmPublication.

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata.  # noqa: E501

        :param repo_gpgcheck: The repo_gpgcheck of this RpmRpmPublication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                repo_gpgcheck is not None and repo_gpgcheck > 1):  # noqa: E501
            raise ValueError("Invalid value for `repo_gpgcheck`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                repo_gpgcheck is not None and repo_gpgcheck < 0):  # noqa: E501
            raise ValueError("Invalid value for `repo_gpgcheck`, must be a value greater than or equal to `0`")  # noqa: E501

        self._repo_gpgcheck = repo_gpgcheck

    @property
    def repo_config(self):
        """Gets the repo_config of this RpmRpmPublication.  # noqa: E501

        A JSON document describing config.repo file  # noqa: E501

        :return: The repo_config of this RpmRpmPublication.  # noqa: E501
        :rtype: object
        """
        return self._repo_config

    @repo_config.setter
    def repo_config(self, repo_config):
        """Sets the repo_config of this RpmRpmPublication.

        A JSON document describing config.repo file  # noqa: E501

        :param repo_config: The repo_config of this RpmRpmPublication.  # noqa: E501
        :type: object
        """

        self._repo_config = repo_config

    @property
    def compression_type(self):
        """Gets the compression_type of this RpmRpmPublication.  # noqa: E501

        The compression type to use for metadata files.  * `zstd` - zstd * `gz` - gz  # noqa: E501

        :return: The compression_type of this RpmRpmPublication.  # noqa: E501
        :rtype: CompressionTypeEnum
        """
        return self._compression_type

    @compression_type.setter
    def compression_type(self, compression_type):
        """Sets the compression_type of this RpmRpmPublication.

        The compression type to use for metadata files.  * `zstd` - zstd * `gz` - gz  # noqa: E501

        :param compression_type: The compression_type of this RpmRpmPublication.  # noqa: E501
        :type: CompressionTypeEnum
        """

        self._compression_type = compression_type

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
        if not isinstance(other, RpmRpmPublication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmRpmPublication):
            return True

        return self.to_dict() != other.to_dict()
