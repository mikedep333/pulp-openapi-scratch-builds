# GemGemContentResponse

A Serializer for GemContent.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**artifacts** | [**object**](.md) | A dict mapping relative paths inside the Content to the correspondingArtifact URLs. E.g.: {&#39;relative/path&#39;: &#39;/artifacts/1/&#39; | [readonly] 
**checksum** | **str** | SHA256 checksum of the gem | [optional] [readonly] 
**name** | **str** | Name of the gem | [optional] [readonly] 
**version** | **str** | Version of the gem | [optional] [readonly] 
**platform** | **str** | Platform of the gem | [optional] [readonly] 
**prerelease** | **bool** | Whether the gem is a prerelease | [optional] [readonly] 
**dependencies** | **dict(str, str)** |  | [optional] [readonly] 
**required_ruby_version** | **str** | Required ruby version of the gem | [optional] [readonly] 
**required_rubygems_version** | **str** | Required rubygems version of the gem | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


