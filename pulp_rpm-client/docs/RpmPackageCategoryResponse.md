# RpmPackageCategoryResponse

PackageCategory serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**id** | **str** | Category id. | 
**name** | **str** | Category name. | 
**description** | **str** | Category description. | 
**display_order** | **int** | Category display order. | 
**group_ids** | [**object**](.md) | Category group list. | 
**desc_by_lang** | [**object**](.md) | Category description by language. | 
**name_by_lang** | [**object**](.md) | Category name by language. | 
**digest** | **str** | Category digest. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


