# OrphansCleanup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_hrefs** | **list[object]** | Will delete specified content and associated Artifacts if they are orphans. | [optional] 
**orphan_protection_time** | **int** | The time in minutes for how long Pulp will hold orphan Content and Artifacts before they become candidates for deletion by this orphan cleanup task. This should ideally be longer than your longest running task otherwise any content created during that task could be cleaned up before the task finishes. If not specified, a default value is taken from the setting ORPHAN_PROTECTION_TIME. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


