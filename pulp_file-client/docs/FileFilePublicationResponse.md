# FileFilePublicationResponse

Serializer for File Publications.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 
**distributions** | **list[str]** | This publication is currently hosted as defined by these distributions. | [optional] [readonly] 
**manifest** | **str** | Filename to use for manifest file containing metadata for all the files. | [optional] [default to 'PULP_MANIFEST']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


