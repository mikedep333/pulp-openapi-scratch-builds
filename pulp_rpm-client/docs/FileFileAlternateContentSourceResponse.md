# FileFileAlternateContentSourceResponse

Serializer for File alternate content source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | Name of Alternate Content Source. | 
**last_refreshed** | **datetime** | Date of last refresh of AlternateContentSource. | [optional] 
**paths** | **list[str]** | List of paths that will be appended to the Remote url when searching for content. | [optional] 
**remote** | **str** | The remote to provide alternate content source. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


