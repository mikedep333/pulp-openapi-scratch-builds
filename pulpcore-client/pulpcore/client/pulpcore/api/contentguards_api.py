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

from pulpcore.client.pulpcore.api_client import ApiClient
from pulpcore.client.pulpcore.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ContentguardsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list(self, pulp_domain="default", **kwargs):  # noqa: E501
        """List content guards  # noqa: E501

        Endpoint to list all contentguards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(pulp_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param str name__contains: Filter results where name contains value
        :param str name__icontains: Filter results where name contains value
        :param str name__iexact: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param str name__iregex: Filter results where name matches regex value
        :param str name__istartswith: Filter results where name starts with value
        :param str name__regex: Filter results where name matches regex value
        :param str name__startswith: Filter results where name starts with value
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `description` - Description * `-description` - Description (descending) * `pk` - Pk * `-pk` - Pk (descending)
        :param list[str] pulp_href__in: Multiple values may be separated by commas.
        :param list[str] pulp_id__in: Multiple values may be separated by commas.
        :param str pulp_type: Pulp type  * `core.rbac` - core.rbac * `core.content_redirect` - core.content_redirect * `core.header` - core.header * `core.composite` - core.composite * `certguard.rhsm` - certguard.rhsm * `certguard.x509` - certguard.x509
        :param list[str] pulp_type__in: Multiple values may be separated by commas.  * `core.rbac` - core.rbac * `core.content_redirect` - core.content_redirect * `core.header` - core.header * `core.composite` - core.composite * `certguard.rhsm` - certguard.rhsm * `certguard.x509` - certguard.x509
        :param str q:
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedContentGuardResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(pulp_domain=pulp_domain, **kwargs)  # noqa: E501

    def list_with_http_info(self, pulp_domain="default", **kwargs):  # noqa: E501
        """List content guards  # noqa: E501

        Endpoint to list all contentguards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(pulp_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param str name__contains: Filter results where name contains value
        :param str name__icontains: Filter results where name contains value
        :param str name__iexact: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param str name__iregex: Filter results where name matches regex value
        :param str name__istartswith: Filter results where name starts with value
        :param str name__regex: Filter results where name matches regex value
        :param str name__startswith: Filter results where name starts with value
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `description` - Description * `-description` - Description (descending) * `pk` - Pk * `-pk` - Pk (descending)
        :param list[str] pulp_href__in: Multiple values may be separated by commas.
        :param list[str] pulp_id__in: Multiple values may be separated by commas.
        :param str pulp_type: Pulp type  * `core.rbac` - core.rbac * `core.content_redirect` - core.content_redirect * `core.header` - core.header * `core.composite` - core.composite * `certguard.rhsm` - certguard.rhsm * `certguard.x509` - certguard.x509
        :param list[str] pulp_type__in: Multiple values may be separated by commas.  * `core.rbac` - core.rbac * `core.content_redirect` - core.content_redirect * `core.header` - core.header * `core.composite` - core.composite * `certguard.rhsm` - certguard.rhsm * `certguard.x509` - certguard.x509
        :param str q:
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedContentGuardResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'pulp_domain',
            'limit',
            'name',
            'name__contains',
            'name__icontains',
            'name__iexact',
            'name__in',
            'name__iregex',
            'name__istartswith',
            'name__regex',
            'name__startswith',
            'offset',
            'ordering',
            'pulp_href__in',
            'pulp_id__in',
            'pulp_type',
            'pulp_type__in',
            'q',
            'fields',
            'exclude_fields'
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
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pulp_domain' is set
        if self.api_client.client_side_validation and ('pulp_domain' not in local_var_params or  # noqa: E501
                                                        local_var_params['pulp_domain'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pulp_domain` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pulp_domain' in local_var_params:
            path_params['pulp_domain'] = local_var_params['pulp_domain']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name__contains' in local_var_params and local_var_params['name__contains'] is not None:  # noqa: E501
            query_params.append(('name__contains', local_var_params['name__contains']))  # noqa: E501
        if 'name__icontains' in local_var_params and local_var_params['name__icontains'] is not None:  # noqa: E501
            query_params.append(('name__icontains', local_var_params['name__icontains']))  # noqa: E501
        if 'name__iexact' in local_var_params and local_var_params['name__iexact'] is not None:  # noqa: E501
            query_params.append(('name__iexact', local_var_params['name__iexact']))  # noqa: E501
        if 'name__in' in local_var_params and local_var_params['name__in'] is not None:  # noqa: E501
            query_params.append(('name__in', local_var_params['name__in']))  # noqa: E501
            collection_formats['name__in'] = 'csv'  # noqa: E501
        if 'name__iregex' in local_var_params and local_var_params['name__iregex'] is not None:  # noqa: E501
            query_params.append(('name__iregex', local_var_params['name__iregex']))  # noqa: E501
        if 'name__istartswith' in local_var_params and local_var_params['name__istartswith'] is not None:  # noqa: E501
            query_params.append(('name__istartswith', local_var_params['name__istartswith']))  # noqa: E501
        if 'name__regex' in local_var_params and local_var_params['name__regex'] is not None:  # noqa: E501
            query_params.append(('name__regex', local_var_params['name__regex']))  # noqa: E501
        if 'name__startswith' in local_var_params and local_var_params['name__startswith'] is not None:  # noqa: E501
            query_params.append(('name__startswith', local_var_params['name__startswith']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
            collection_formats['ordering'] = 'csv'  # noqa: E501
        if 'pulp_href__in' in local_var_params and local_var_params['pulp_href__in'] is not None:  # noqa: E501
            query_params.append(('pulp_href__in', local_var_params['pulp_href__in']))  # noqa: E501
            collection_formats['pulp_href__in'] = 'csv'  # noqa: E501
        if 'pulp_id__in' in local_var_params and local_var_params['pulp_id__in'] is not None:  # noqa: E501
            query_params.append(('pulp_id__in', local_var_params['pulp_id__in']))  # noqa: E501
            collection_formats['pulp_id__in'] = 'csv'  # noqa: E501
        if 'pulp_type' in local_var_params and local_var_params['pulp_type'] is not None:  # noqa: E501
            query_params.append(('pulp_type', local_var_params['pulp_type']))  # noqa: E501
        if 'pulp_type__in' in local_var_params and local_var_params['pulp_type__in'] is not None:  # noqa: E501
            query_params.append(('pulp_type__in', local_var_params['pulp_type__in']))  # noqa: E501
            collection_formats['pulp_type__in'] = 'csv'  # noqa: E501
        if 'q' in local_var_params and local_var_params['q'] is not None:  # noqa: E501
            query_params.append(('q', local_var_params['q']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/pulp/{pulp_domain}/api/v3/contentguards/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedContentGuardResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
