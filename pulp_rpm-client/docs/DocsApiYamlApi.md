# pulpcore.client.pulp_rpm.DocsApiYamlApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docs_api_yaml_get**](DocsApiYamlApi.md#docs_api_yaml_get) | **GET** /api/pulp/api/v3/docs/api.yaml | 


# **docs_api_yaml_get**
> object docs_api_yaml_get(lang=lang, fields=fields, exclude_fields=exclude_fields)



OpenApi3 schema for this API. Format can be selected via content negotiation.  - YAML: application/vnd.oai.openapi - JSON: application/vnd.oai.openapi+json

### Example

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


# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.DocsApiYamlApi(api_client)
    lang = 'lang_example' # str |  (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        api_response = api_instance.docs_api_yaml_get(lang=lang, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocsApiYamlApi->docs_api_yaml_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**|  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.oai.openapi, application/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

