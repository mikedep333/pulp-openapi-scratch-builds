# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_rpm.api_client import ApiClient
from pulpcore.client.pulp_rpm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OrphansApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def orphans_delete(self, pulp_domain="default", **kwargs):  # noqa: E501
        """Delete orphans  # noqa: E501

        DEPRECATED! Trigger an asynchronous task that deletes all orphaned content and artifacts. Use the `POST /pulp/api/v3/orphans/cleanup/` call instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orphans_delete(pulp_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.orphans_delete_with_http_info(pulp_domain=pulp_domain, **kwargs)  # noqa: E501

    def orphans_delete_with_http_info(self, pulp_domain="default", **kwargs):  # noqa: E501
        """Delete orphans  # noqa: E501

        DEPRECATED! Trigger an asynchronous task that deletes all orphaned content and artifacts. Use the `POST /pulp/api/v3/orphans/cleanup/` call instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orphans_delete_with_http_info(pulp_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'pulp_domain'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orphans_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pulp_domain' is set
        if self.api_client.client_side_validation and ('pulp_domain' not in local_var_params or  # noqa: E501
                                                        local_var_params['pulp_domain'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pulp_domain` when calling `orphans_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pulp_domain' in local_var_params:
            path_params['pulp_domain'] = local_var_params['pulp_domain']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth', 'json_header_remote_authentication']  # noqa: E501

        return self.api_client.call_api(
            '/api/pulp/{pulp_domain}/api/v3/orphans/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
