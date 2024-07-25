# pulpcore.client.pulp_rpm.PublicationsPypiApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publications_python_pypi_add_role**](PublicationsPypiApi.md#publications_python_pypi_add_role) | **POST** {python_python_publication_href}add_role/ | Add a role
[**publications_python_pypi_create**](PublicationsPypiApi.md#publications_python_pypi_create) | **POST** /api/pulp/{pulp_domain}/api/v3/publications/python/pypi/ | Create a python publication
[**publications_python_pypi_delete**](PublicationsPypiApi.md#publications_python_pypi_delete) | **DELETE** {python_python_publication_href} | Delete a python publication
[**publications_python_pypi_list**](PublicationsPypiApi.md#publications_python_pypi_list) | **GET** /api/pulp/{pulp_domain}/api/v3/publications/python/pypi/ | List python publications
[**publications_python_pypi_list_roles**](PublicationsPypiApi.md#publications_python_pypi_list_roles) | **GET** {python_python_publication_href}list_roles/ | List roles
[**publications_python_pypi_my_permissions**](PublicationsPypiApi.md#publications_python_pypi_my_permissions) | **GET** {python_python_publication_href}my_permissions/ | List user permissions
[**publications_python_pypi_read**](PublicationsPypiApi.md#publications_python_pypi_read) | **GET** {python_python_publication_href} | Inspect a python publication
[**publications_python_pypi_remove_role**](PublicationsPypiApi.md#publications_python_pypi_remove_role) | **POST** {python_python_publication_href}remove_role/ | Remove a role


# **publications_python_pypi_add_role**
> NestedRoleResponse publications_python_pypi_add_role(python_python_publication_href, nested_role)

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.publications_python_pypi_add_role(python_python_publication_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_add_role: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.publications_python_pypi_add_role(python_python_publication_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_add_role: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.publications_python_pypi_add_role(python_python_publication_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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

# **publications_python_pypi_create**
> AsyncOperationResponse publications_python_pypi_create(pulp_domain, python_python_publication)

Create a python publication

 Dispatches a publish task, which generates metadata that will be used by pip.

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
python_python_publication = pulpcore.client.pulp_rpm.PythonPythonPublication() # PythonPythonPublication | 

    try:
        # Create a python publication
        api_response = api_instance.publications_python_pypi_create(pulp_domain, python_python_publication)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
python_python_publication = pulpcore.client.pulp_rpm.PythonPythonPublication() # PythonPythonPublication | 

    try:
        # Create a python publication
        api_response = api_instance.publications_python_pypi_create(pulp_domain, python_python_publication)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
python_python_publication = pulpcore.client.pulp_rpm.PythonPythonPublication() # PythonPythonPublication | 

    try:
        # Create a python publication
        api_response = api_instance.publications_python_pypi_create(pulp_domain, python_python_publication)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **python_python_publication** | [**PythonPythonPublication**](PythonPythonPublication.md)|  | 

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

# **publications_python_pypi_delete**
> publications_python_pypi_delete(python_python_publication_href)

Delete a python publication

 Python Publications refer to the Python Package content in a repository version, and include metadata about that content.

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 

    try:
        # Delete a python publication
        api_instance.publications_python_pypi_delete(python_python_publication_href)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_delete: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 

    try:
        # Delete a python publication
        api_instance.publications_python_pypi_delete(python_python_publication_href)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_delete: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 

    try:
        # Delete a python publication
        api_instance.publications_python_pypi_delete(python_python_publication_href)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publications_python_pypi_list**
> PaginatedpythonPythonPublicationResponseList publications_python_pypi_list(pulp_domain, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)

List python publications

 Python Publications refer to the Python Package content in a repository version, and include metadata about that content.

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
content = 'content_example' # str | Content Unit referenced by HREF (optional)
content__in = 'content__in_example' # str | Content Unit referenced by HREF (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `complete` - Complete * `-complete` - Complete (descending) * `pass_through` - Pass through * `-pass_through` - Pass through (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_created = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created matches value (optional)
pulp_created__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than value (optional)
pulp_created__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than or equal to value (optional)
pulp_created__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than value (optional)
pulp_created__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than or equal to value (optional)
pulp_created__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where pulp_created is between two comma separated values (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository = 'repository_example' # str | Repository referenced by HREF (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List python publications
        api_response = api_instance.publications_python_pypi_list(pulp_domain, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_list: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
content = 'content_example' # str | Content Unit referenced by HREF (optional)
content__in = 'content__in_example' # str | Content Unit referenced by HREF (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `complete` - Complete * `-complete` - Complete (descending) * `pass_through` - Pass through * `-pass_through` - Pass through (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_created = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created matches value (optional)
pulp_created__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than value (optional)
pulp_created__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than or equal to value (optional)
pulp_created__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than value (optional)
pulp_created__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than or equal to value (optional)
pulp_created__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where pulp_created is between two comma separated values (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository = 'repository_example' # str | Repository referenced by HREF (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List python publications
        api_response = api_instance.publications_python_pypi_list(pulp_domain, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_list: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
content = 'content_example' # str | Content Unit referenced by HREF (optional)
content__in = 'content__in_example' # str | Content Unit referenced by HREF (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `complete` - Complete * `-complete` - Complete (descending) * `pass_through` - Pass through * `-pass_through` - Pass through (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_created = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created matches value (optional)
pulp_created__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than value (optional)
pulp_created__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than or equal to value (optional)
pulp_created__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than value (optional)
pulp_created__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than or equal to value (optional)
pulp_created__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where pulp_created is between two comma separated values (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository = 'repository_example' # str | Repository referenced by HREF (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List python publications
        api_response = api_instance.publications_python_pypi_list(pulp_domain, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **content** | **str**| Content Unit referenced by HREF | [optional] 
 **content__in** | **str**| Content Unit referenced by HREF | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;complete&#x60; - Complete * &#x60;-complete&#x60; - Complete (descending) * &#x60;pass_through&#x60; - Pass through * &#x60;-pass_through&#x60; - Pass through (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **pulp_created** | **datetime**| Filter results where pulp_created matches value | [optional] 
 **pulp_created__gt** | **datetime**| Filter results where pulp_created is greater than value | [optional] 
 **pulp_created__gte** | **datetime**| Filter results where pulp_created is greater than or equal to value | [optional] 
 **pulp_created__lt** | **datetime**| Filter results where pulp_created is less than value | [optional] 
 **pulp_created__lte** | **datetime**| Filter results where pulp_created is less than or equal to value | [optional] 
 **pulp_created__range** | [**list[datetime]**](datetime.md)| Filter results where pulp_created is between two comma separated values | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **repository** | **str**| Repository referenced by HREF | [optional] 
 **repository_version** | [**str**](.md)| Repository Version referenced by HREF | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedpythonPythonPublicationResponseList**](PaginatedpythonPythonPublicationResponseList.md)

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

# **publications_python_pypi_list_roles**
> ObjectRolesResponse publications_python_pypi_list_roles(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.publications_python_pypi_list_roles(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_list_roles: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.publications_python_pypi_list_roles(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_list_roles: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.publications_python_pypi_list_roles(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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

# **publications_python_pypi_my_permissions**
> MyPermissionsResponse publications_python_pypi_my_permissions(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.publications_python_pypi_my_permissions(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_my_permissions: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.publications_python_pypi_my_permissions(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_my_permissions: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.publications_python_pypi_my_permissions(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_my_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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

# **publications_python_pypi_read**
> PythonPythonPublicationResponse publications_python_pypi_read(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)

Inspect a python publication

 Python Publications refer to the Python Package content in a repository version, and include metadata about that content.

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a python publication
        api_response = api_instance.publications_python_pypi_read(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_read: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a python publication
        api_response = api_instance.publications_python_pypi_read(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_read: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a python publication
        api_response = api_instance.publications_python_pypi_read(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PythonPythonPublicationResponse**](PythonPythonPublicationResponse.md)

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

# **publications_python_pypi_remove_role**
> NestedRoleResponse publications_python_pypi_remove_role(python_python_publication_href, nested_role)

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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.publications_python_pypi_remove_role(python_python_publication_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_remove_role: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.publications_python_pypi_remove_role(python_python_publication_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_remove_role: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.publications_python_pypi_remove_role(python_python_publication_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicationsPypiApi->publications_python_pypi_remove_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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

