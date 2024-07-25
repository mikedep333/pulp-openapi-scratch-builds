# pulpcore.client.pulp_rpm.PypiLegacyApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pypi_legacy_create**](PypiLegacyApi.md#pypi_legacy_create) | **POST** /pypi/{pulp_domain}/{path}/legacy/ | Upload a package


# **pypi_legacy_create**
> PackageUploadTaskResponse pypi_legacy_create(path, pulp_domain, content, sha256_digest, action=action)

Upload a package

Upload package to the index.  This is the endpoint that tools like Twine and Poetry use for their upload commands.

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
    api_instance = pulpcore.client.pulp_rpm.PypiLegacyApi(api_client)
    path = 'path_example' # str | 
pulp_domain = 'pulp_domain_example' # str | 
content = '/path/to/file' # file | A Python package release file to upload to the index.
sha256_digest = 'sha256_digest_example' # str | SHA256 of package to validate upload integrity.
action = 'file_upload' # str | Defaults to `file_upload`, don't change it or request will fail! (optional) (default to 'file_upload')

    try:
        # Upload a package
        api_response = api_instance.pypi_legacy_create(path, pulp_domain, content, sha256_digest, action=action)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PypiLegacyApi->pypi_legacy_create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PypiLegacyApi(api_client)
    path = 'path_example' # str | 
pulp_domain = 'pulp_domain_example' # str | 
content = '/path/to/file' # file | A Python package release file to upload to the index.
sha256_digest = 'sha256_digest_example' # str | SHA256 of package to validate upload integrity.
action = 'file_upload' # str | Defaults to `file_upload`, don't change it or request will fail! (optional) (default to 'file_upload')

    try:
        # Upload a package
        api_response = api_instance.pypi_legacy_create(path, pulp_domain, content, sha256_digest, action=action)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PypiLegacyApi->pypi_legacy_create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.PypiLegacyApi(api_client)
    path = 'path_example' # str | 
pulp_domain = 'pulp_domain_example' # str | 
content = '/path/to/file' # file | A Python package release file to upload to the index.
sha256_digest = 'sha256_digest_example' # str | SHA256 of package to validate upload integrity.
action = 'file_upload' # str | Defaults to `file_upload`, don't change it or request will fail! (optional) (default to 'file_upload')

    try:
        # Upload a package
        api_response = api_instance.pypi_legacy_create(path, pulp_domain, content, sha256_digest, action=action)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PypiLegacyApi->pypi_legacy_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **pulp_domain** | **str**|  | 
 **content** | **file**| A Python package release file to upload to the index. | 
 **sha256_digest** | **str**| SHA256 of package to validate upload integrity. | 
 **action** | **str**| Defaults to &#x60;file_upload&#x60;, don&#39;t change it or request will fail! | [optional] [default to &#39;file_upload&#39;]

### Return type

[**PackageUploadTaskResponse**](PackageUploadTaskResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

