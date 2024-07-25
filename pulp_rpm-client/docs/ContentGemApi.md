# pulpcore.client.pulp_rpm.ContentGemApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_gem_gem_create**](ContentGemApi.md#content_gem_gem_create) | **POST** /api/pulp/{pulp_domain}/api/v3/content/gem/gem/ | Create a gem content
[**content_gem_gem_list**](ContentGemApi.md#content_gem_gem_list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/gem/gem/ | List gem contents
[**content_gem_gem_read**](ContentGemApi.md#content_gem_gem_read) | **GET** {gem_gem_content_href} | Inspect a gem content


# **content_gem_gem_create**
> AsyncOperationResponse content_gem_gem_create(pulp_domain, repository=repository, artifact=artifact, file=file)

Create a gem content

Trigger an asynchronous task to create content,optionally create new repository version.

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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
file = '/path/to/file' # file | An uploaded file that should be turned into the artifact of the content unit. (optional)

    try:
        # Create a gem content
        api_response = api_instance.content_gem_gem_create(pulp_domain, repository=repository, artifact=artifact, file=file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
file = '/path/to/file' # file | An uploaded file that should be turned into the artifact of the content unit. (optional)

    try:
        # Create a gem content
        api_response = api_instance.content_gem_gem_create(pulp_domain, repository=repository, artifact=artifact, file=file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
file = '/path/to/file' # file | An uploaded file that should be turned into the artifact of the content unit. (optional)

    try:
        # Create a gem content
        api_response = api_instance.content_gem_gem_create(pulp_domain, repository=repository, artifact=artifact, file=file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **repository** | **str**| A URI of a repository the new content unit should be associated with. | [optional] 
 **artifact** | **str**| Artifact file representing the physical content | [optional] 
 **file** | **file**| An uploaded file that should be turned into the artifact of the content unit. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gem_gem_list**
> PaginatedgemGemContentResponseList content_gem_gem_list(pulp_domain, checksum=checksum, limit=limit, name=name, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prerelease=prerelease, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, version=version, fields=fields, exclude_fields=exclude_fields)

List gem contents

A ViewSet for GemContent.

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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
checksum = 'checksum_example' # str | Filter results where checksum matches value (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `version` - Version * `-version` - Version (descending) * `platform` - Platform * `-platform` - Platform (descending) * `checksum` - Checksum * `-checksum` - Checksum (descending) * `prerelease` - Prerelease * `-prerelease` - Prerelease (descending) * `dependencies` - Dependencies * `-dependencies` - Dependencies (descending) * `required_ruby_version` - Required ruby version * `-required_ruby_version` - Required ruby version (descending) * `required_rubygems_version` - Required rubygems version * `-required_rubygems_version` - Required rubygems version (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
prerelease = True # bool | Filter results where prerelease matches value (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
version = 'version_example' # str | Filter results where version matches value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List gem contents
        api_response = api_instance.content_gem_gem_list(pulp_domain, checksum=checksum, limit=limit, name=name, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prerelease=prerelease, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, version=version, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_list: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
checksum = 'checksum_example' # str | Filter results where checksum matches value (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `version` - Version * `-version` - Version (descending) * `platform` - Platform * `-platform` - Platform (descending) * `checksum` - Checksum * `-checksum` - Checksum (descending) * `prerelease` - Prerelease * `-prerelease` - Prerelease (descending) * `dependencies` - Dependencies * `-dependencies` - Dependencies (descending) * `required_ruby_version` - Required ruby version * `-required_ruby_version` - Required ruby version (descending) * `required_rubygems_version` - Required rubygems version * `-required_rubygems_version` - Required rubygems version (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
prerelease = True # bool | Filter results where prerelease matches value (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
version = 'version_example' # str | Filter results where version matches value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List gem contents
        api_response = api_instance.content_gem_gem_list(pulp_domain, checksum=checksum, limit=limit, name=name, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prerelease=prerelease, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, version=version, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_list: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
checksum = 'checksum_example' # str | Filter results where checksum matches value (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `version` - Version * `-version` - Version (descending) * `platform` - Platform * `-platform` - Platform (descending) * `checksum` - Checksum * `-checksum` - Checksum (descending) * `prerelease` - Prerelease * `-prerelease` - Prerelease (descending) * `dependencies` - Dependencies * `-dependencies` - Dependencies (descending) * `required_ruby_version` - Required ruby version * `-required_ruby_version` - Required ruby version (descending) * `required_rubygems_version` - Required rubygems version * `-required_rubygems_version` - Required rubygems version (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
prerelease = True # bool | Filter results where prerelease matches value (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
version = 'version_example' # str | Filter results where version matches value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List gem contents
        api_response = api_instance.content_gem_gem_list(pulp_domain, checksum=checksum, limit=limit, name=name, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prerelease=prerelease, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, version=version, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **checksum** | **str**| Filter results where checksum matches value | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;platform&#x60; - Platform * &#x60;-platform&#x60; - Platform (descending) * &#x60;checksum&#x60; - Checksum * &#x60;-checksum&#x60; - Checksum (descending) * &#x60;prerelease&#x60; - Prerelease * &#x60;-prerelease&#x60; - Prerelease (descending) * &#x60;dependencies&#x60; - Dependencies * &#x60;-dependencies&#x60; - Dependencies (descending) * &#x60;required_ruby_version&#x60; - Required ruby version * &#x60;-required_ruby_version&#x60; - Required ruby version (descending) * &#x60;required_rubygems_version&#x60; - Required rubygems version * &#x60;-required_rubygems_version&#x60; - Required rubygems version (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **prerelease** | **bool**| Filter results where prerelease matches value | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **version** | **str**| Filter results where version matches value | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedgemGemContentResponseList**](PaginatedgemGemContentResponseList.md)

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

# **content_gem_gem_read**
> GemGemContentResponse content_gem_gem_read(gem_gem_content_href, fields=fields, exclude_fields=exclude_fields)

Inspect a gem content

A ViewSet for GemContent.

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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    gem_gem_content_href = 'gem_gem_content_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a gem content
        api_response = api_instance.content_gem_gem_read(gem_gem_content_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_read: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    gem_gem_content_href = 'gem_gem_content_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a gem content
        api_response = api_instance.content_gem_gem_read(gem_gem_content_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_read: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentGemApi(api_client)
    gem_gem_content_href = 'gem_gem_content_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a gem content
        api_response = api_instance.content_gem_gem_read(gem_gem_content_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentGemApi->content_gem_gem_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_content_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**GemGemContentResponse**](GemGemContentResponse.md)

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

