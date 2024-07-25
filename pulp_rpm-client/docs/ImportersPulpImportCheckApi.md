# pulpcore.client.pulp_rpm.ImportersPulpImportCheckApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pulp_import_check_post**](ImportersPulpImportCheckApi.md#pulp_import_check_post) | **POST** /api/pulp/{pulp_domain}/api/v3/importers/core/pulp/import-check/ | Validate the parameters to be used for a PulpImport call


# **pulp_import_check_post**
> PulpImportCheckResponse pulp_import_check_post(pulp_domain, pulp_import_check)

Validate the parameters to be used for a PulpImport call

Evaluates validity of proposed PulpImport parameters 'toc', 'path', and 'repo_mapping'.  * Checks that toc, path are in ALLOWED_IMPORT_PATHS * if ALLOWED:   * Checks that toc, path exist and are readable   * If toc specified, checks that containing dir is writeable * Checks that repo_mapping is valid JSON

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
    api_instance = pulpcore.client.pulp_rpm.ImportersPulpImportCheckApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
pulp_import_check = pulpcore.client.pulp_rpm.PulpImportCheck() # PulpImportCheck | 

    try:
        # Validate the parameters to be used for a PulpImport call
        api_response = api_instance.pulp_import_check_post(pulp_domain, pulp_import_check)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportersPulpImportCheckApi->pulp_import_check_post: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ImportersPulpImportCheckApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
pulp_import_check = pulpcore.client.pulp_rpm.PulpImportCheck() # PulpImportCheck | 

    try:
        # Validate the parameters to be used for a PulpImport call
        api_response = api_instance.pulp_import_check_post(pulp_domain, pulp_import_check)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportersPulpImportCheckApi->pulp_import_check_post: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ImportersPulpImportCheckApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
pulp_import_check = pulpcore.client.pulp_rpm.PulpImportCheck() # PulpImportCheck | 

    try:
        # Validate the parameters to be used for a PulpImport call
        api_response = api_instance.pulp_import_check_post(pulp_domain, pulp_import_check)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportersPulpImportCheckApi->pulp_import_check_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **pulp_import_check** | [**PulpImportCheck**](PulpImportCheck.md)|  | 

### Return type

[**PulpImportCheckResponse**](PulpImportCheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

