# PythonPythonPackageContent

A Serializer for PythonPackageContent.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**relative_path** | **str** | Path where the artifact is located relative to distributions base_path | 
**file** | **file** | An uploaded file that may be turned into the content unit. | [optional] 
**upload** | **str** | An uncommitted upload that may be turned into the content unit. | [optional] 
**url** | **str** | A url that Pulp can download and turn into the content unit. | [optional] 
**sha256** | **str** | The SHA256 digest of this package. | [optional] [default to '']
**summary** | **str** | A one-line summary of what the package does. | [optional] 
**description** | **str** | A longer description of the package that can run to several paragraphs. | [optional] 
**description_content_type** | **str** | A string stating the markup syntax (if any) used in the distribution’s description, so that tools can intelligently render the description. | [optional] 
**keywords** | **str** | Additional keywords to be used to assist searching for the package in a larger catalog. | [optional] 
**home_page** | **str** | The URL for the package&#39;s home page. | [optional] 
**download_url** | **str** | Legacy field denoting the URL from which this package can be downloaded. | [optional] 
**author** | **str** | Text containing the author&#39;s name. Contact information can also be added, separated with newlines. | [optional] 
**author_email** | **str** | The author&#39;s e-mail address.  | [optional] 
**maintainer** | **str** | The maintainer&#39;s name at a minimum; additional contact information may be provided. | [optional] 
**maintainer_email** | **str** | The maintainer&#39;s e-mail address. | [optional] 
**license** | **str** | Text indicating the license covering the distribution | [optional] 
**requires_python** | **str** | The Python version(s) that the distribution is guaranteed to be compatible with. | [optional] 
**project_url** | **str** | A browsable URL for the project and a label for it, separated by a comma. | [optional] 
**project_urls** | [**object**](.md) | A dictionary of labels and URLs for the project. | [optional] 
**platform** | **str** | A comma-separated list of platform specifications, summarizing the operating systems supported by the package. | [optional] 
**supported_platform** | **str** | Field to specify the OS and CPU for which the binary package was compiled.  | [optional] 
**requires_dist** | [**object**](.md) | A JSON list containing names of some other distutils project required by this distribution. | [optional] 
**provides_dist** | [**object**](.md) | A JSON list containing names of a Distutils project which is contained within this distribution. | [optional] 
**obsoletes_dist** | [**object**](.md) | A JSON list containing names of a distutils project&#39;s distribution which this distribution renders obsolete, meaning that the two projects should not be installed at the same time. | [optional] 
**requires_external** | [**object**](.md) | A JSON list containing some dependency in the system that the distribution is to be used. | [optional] 
**classifiers** | [**object**](.md) | A JSON list containing classification values for a Python package. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


