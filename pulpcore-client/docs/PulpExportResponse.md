# PulpExportResponse

Serializer for PulpExports.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**task** | **str** | A URI of the task that ran the Export. | [optional] 
**exported_resources** | **list[str]** | Resources that were exported. | [optional] [readonly] 
**params** | [**object**](.md) | Any additional parameters that were used to create the export. | [optional] [readonly] 
**output_file_info** | [**object**](.md) | Dictionary of filename: sha256hash entries for export-output-file(s) | [optional] [readonly] 
**toc_info** | [**object**](.md) | Filename and sha256-checksum of table-of-contents for this export | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


