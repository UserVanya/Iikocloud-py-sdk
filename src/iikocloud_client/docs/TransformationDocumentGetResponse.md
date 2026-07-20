# TransformationDocumentGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**assembly_chart_writeoff** | **bool** |  | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[TransformationDocumentGetItem]**](TransformationDocumentGetItem.md) | List of document items | [optional] 
**number** | **str** | Document number | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**store_from** | **str** | Write-off store identifier (GUID) | [optional] 
**store_to** | **str** | Receipt store identifier (GUID) | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.transformation_document_get_response import TransformationDocumentGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransformationDocumentGetResponse from a JSON string
transformation_document_get_response_instance = TransformationDocumentGetResponse.from_json(json)
# print the JSON string representation of the object
print(TransformationDocumentGetResponse.to_json())

# convert the object into a dict
transformation_document_get_response_dict = transformation_document_get_response_instance.to_dict()
# create an instance of TransformationDocumentGetResponse from a dict
transformation_document_get_response_from_dict = TransformationDocumentGetResponse.from_dict(transformation_document_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


