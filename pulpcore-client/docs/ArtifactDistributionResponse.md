# ArtifactDistributionResponse

A serializer for ArtifactDistribution.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | 
**pulp_href** | **str** |  | [optional] [readonly] 
**base_url** | **str** | The URL for accessing the publication as defined by this distribution. | [optional] [readonly] 
**pulp_labels** | **dict(str, str)** |  | [optional] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


