# pulpcore.client.pulp_rpm.AcsFileApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acs_file_file_add_role**](AcsFileApi.md#acs_file_file_add_role) | **POST** {file_file_alternate_content_source_href}add_role/ | Add a role
[**acs_file_file_create**](AcsFileApi.md#acs_file_file_create) | **POST** /api/pulp/{pulp_domain}/api/v3/acs/file/file/ | Create a file alternate content source
[**acs_file_file_delete**](AcsFileApi.md#acs_file_file_delete) | **DELETE** {file_file_alternate_content_source_href} | Delete a file alternate content source
[**acs_file_file_list**](AcsFileApi.md#acs_file_file_list) | **GET** /api/pulp/{pulp_domain}/api/v3/acs/file/file/ | List file alternate content sources
[**acs_file_file_list_roles**](AcsFileApi.md#acs_file_file_list_roles) | **GET** {file_file_alternate_content_source_href}list_roles/ | List roles
[**acs_file_file_my_permissions**](AcsFileApi.md#acs_file_file_my_permissions) | **GET** {file_file_alternate_content_source_href}my_permissions/ | List user permissions
[**acs_file_file_partial_update**](AcsFileApi.md#acs_file_file_partial_update) | **PATCH** {file_file_alternate_content_source_href} | Update a file alternate content source
[**acs_file_file_read**](AcsFileApi.md#acs_file_file_read) | **GET** {file_file_alternate_content_source_href} | Inspect a file alternate content source
[**acs_file_file_refresh**](AcsFileApi.md#acs_file_file_refresh) | **POST** {file_file_alternate_content_source_href}refresh/ | Refresh metadata
[**acs_file_file_remove_role**](AcsFileApi.md#acs_file_file_remove_role) | **POST** {file_file_alternate_content_source_href}remove_role/ | Remove a role
[**acs_file_file_update**](AcsFileApi.md#acs_file_file_update) | **PUT** {file_file_alternate_content_source_href} | Update a file alternate content source


# **acs_file_file_add_role**
> NestedRoleResponse acs_file_file_add_role(file_file_alternate_content_source_href, nested_role)

Add a role

Add a role for this object to users/groups.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.acs_file_file_add_role(file_file_alternate_content_source_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_add_role: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.acs_file_file_add_role(file_file_alternate_content_source_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_add_role: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.acs_file_file_add_role(file_file_alternate_content_source_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_create**
> FileFileAlternateContentSourceResponse acs_file_file_create(pulp_domain, file_file_alternate_content_source)

Create a file alternate content source

Alternate Content Source ViewSet for File  ACS support is provided as a tech preview in pulp_file.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
file_file_alternate_content_source = pulpcore.client.pulp_rpm.FileFileAlternateContentSource() # FileFileAlternateContentSource | 

    try:
        # Create a file alternate content source
        api_response = api_instance.acs_file_file_create(pulp_domain, file_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_create: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
file_file_alternate_content_source = pulpcore.client.pulp_rpm.FileFileAlternateContentSource() # FileFileAlternateContentSource | 

    try:
        # Create a file alternate content source
        api_response = api_instance.acs_file_file_create(pulp_domain, file_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_create: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
file_file_alternate_content_source = pulpcore.client.pulp_rpm.FileFileAlternateContentSource() # FileFileAlternateContentSource | 

    try:
        # Create a file alternate content source
        api_response = api_instance.acs_file_file_create(pulp_domain, file_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **file_file_alternate_content_source** | [**FileFileAlternateContentSource**](FileFileAlternateContentSource.md)|  | 

### Return type

[**FileFileAlternateContentSourceResponse**](FileFileAlternateContentSourceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_delete**
> AsyncOperationResponse acs_file_file_delete(file_file_alternate_content_source_href)

Delete a file alternate content source

Trigger an asynchronous delete ACS task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 

    try:
        # Delete a file alternate content source
        api_response = api_instance.acs_file_file_delete(file_file_alternate_content_source_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_delete: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 

    try:
        # Delete a file alternate content source
        api_response = api_instance.acs_file_file_delete(file_file_alternate_content_source_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_delete: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 

    try:
        # Delete a file alternate content source
        api_response = api_instance.acs_file_file_delete(file_file_alternate_content_source_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_list**
> PaginatedfileFileAlternateContentSourceResponseList acs_file_file_list(pulp_domain, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, fields=fields, exclude_fields=exclude_fields)

List file alternate content sources

Alternate Content Source ViewSet for File  ACS support is provided as a tech preview in pulp_file.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `last_refreshed` - Last refreshed * `-last_refreshed` - Last refreshed (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List file alternate content sources
        api_response = api_instance.acs_file_file_list(pulp_domain, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `last_refreshed` - Last refreshed * `-last_refreshed` - Last refreshed (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List file alternate content sources
        api_response = api_instance.acs_file_file_list(pulp_domain, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_list: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `last_refreshed` - Last refreshed * `-last_refreshed` - Last refreshed (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List file alternate content sources
        api_response = api_instance.acs_file_file_list(pulp_domain, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **name__icontains** | **str**| Filter results where name contains value | [optional] 
 **name__iexact** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**list[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__iregex** | **str**| Filter results where name matches regex value | [optional] 
 **name__istartswith** | **str**| Filter results where name starts with value | [optional] 
 **name__regex** | **str**| Filter results where name matches regex value | [optional] 
 **name__startswith** | **str**| Filter results where name starts with value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;last_refreshed&#x60; - Last refreshed * &#x60;-last_refreshed&#x60; - Last refreshed (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedfileFileAlternateContentSourceResponseList**](PaginatedfileFileAlternateContentSourceResponseList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_list_roles**
> ObjectRolesResponse acs_file_file_list_roles(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)

List roles

List roles assigned to this object.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.acs_file_file_list_roles(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_list_roles: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.acs_file_file_list_roles(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_list_roles: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.acs_file_file_list_roles(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**ObjectRolesResponse**](ObjectRolesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_my_permissions**
> MyPermissionsResponse acs_file_file_my_permissions(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)

List user permissions

List permissions available to the current user on this object.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.acs_file_file_my_permissions(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_my_permissions: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.acs_file_file_my_permissions(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_my_permissions: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.acs_file_file_my_permissions(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_my_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**MyPermissionsResponse**](MyPermissionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_partial_update**
> AsyncOperationResponse acs_file_file_partial_update(file_file_alternate_content_source_href, patchedfile_file_alternate_content_source)

Update a file alternate content source

Trigger an asynchronous partial update task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
patchedfile_file_alternate_content_source = pulpcore.client.pulp_rpm.PatchedfileFileAlternateContentSource() # PatchedfileFileAlternateContentSource | 

    try:
        # Update a file alternate content source
        api_response = api_instance.acs_file_file_partial_update(file_file_alternate_content_source_href, patchedfile_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_partial_update: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
patchedfile_file_alternate_content_source = pulpcore.client.pulp_rpm.PatchedfileFileAlternateContentSource() # PatchedfileFileAlternateContentSource | 

    try:
        # Update a file alternate content source
        api_response = api_instance.acs_file_file_partial_update(file_file_alternate_content_source_href, patchedfile_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_partial_update: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
patchedfile_file_alternate_content_source = pulpcore.client.pulp_rpm.PatchedfileFileAlternateContentSource() # PatchedfileFileAlternateContentSource | 

    try:
        # Update a file alternate content source
        api_response = api_instance.acs_file_file_partial_update(file_file_alternate_content_source_href, patchedfile_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 
 **patchedfile_file_alternate_content_source** | [**PatchedfileFileAlternateContentSource**](PatchedfileFileAlternateContentSource.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_read**
> FileFileAlternateContentSourceResponse acs_file_file_read(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)

Inspect a file alternate content source

Alternate Content Source ViewSet for File  ACS support is provided as a tech preview in pulp_file.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a file alternate content source
        api_response = api_instance.acs_file_file_read(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_read: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a file alternate content source
        api_response = api_instance.acs_file_file_read(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_read: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a file alternate content source
        api_response = api_instance.acs_file_file_read(file_file_alternate_content_source_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**FileFileAlternateContentSourceResponse**](FileFileAlternateContentSourceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_refresh**
> TaskGroupOperationResponse acs_file_file_refresh(file_file_alternate_content_source_href)

Refresh metadata

Trigger an asynchronous task to create Alternate Content Source content.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 

    try:
        # Refresh metadata
        api_response = api_instance.acs_file_file_refresh(file_file_alternate_content_source_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_refresh: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 

    try:
        # Refresh metadata
        api_response = api_instance.acs_file_file_refresh(file_file_alternate_content_source_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_refresh: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 

    try:
        # Refresh metadata
        api_response = api_instance.acs_file_file_refresh(file_file_alternate_content_source_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 

### Return type

[**TaskGroupOperationResponse**](TaskGroupOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_remove_role**
> NestedRoleResponse acs_file_file_remove_role(file_file_alternate_content_source_href, nested_role)

Remove a role

Remove a role for this object from users/groups.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.acs_file_file_remove_role(file_file_alternate_content_source_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_remove_role: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.acs_file_file_remove_role(file_file_alternate_content_source_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_remove_role: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.acs_file_file_remove_role(file_file_alternate_content_source_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_remove_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acs_file_file_update**
> AsyncOperationResponse acs_file_file_update(file_file_alternate_content_source_href, file_file_alternate_content_source)

Update a file alternate content source

Trigger an asynchronous update task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
file_file_alternate_content_source = pulpcore.client.pulp_rpm.FileFileAlternateContentSource() # FileFileAlternateContentSource | 

    try:
        # Update a file alternate content source
        api_response = api_instance.acs_file_file_update(file_file_alternate_content_source_href, file_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_update: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
file_file_alternate_content_source = pulpcore.client.pulp_rpm.FileFileAlternateContentSource() # FileFileAlternateContentSource | 

    try:
        # Update a file alternate content source
        api_response = api_instance.acs_file_file_update(file_file_alternate_content_source_href, file_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_update: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8000"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsFileApi(api_client)
    file_file_alternate_content_source_href = 'file_file_alternate_content_source_href_example' # str | 
file_file_alternate_content_source = pulpcore.client.pulp_rpm.FileFileAlternateContentSource() # FileFileAlternateContentSource | 

    try:
        # Update a file alternate content source
        api_response = api_instance.acs_file_file_update(file_file_alternate_content_source_href, file_file_alternate_content_source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsFileApi->acs_file_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_file_alternate_content_source_href** | **str**|  | 
 **file_file_alternate_content_source** | [**FileFileAlternateContentSource**](FileFileAlternateContentSource.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
