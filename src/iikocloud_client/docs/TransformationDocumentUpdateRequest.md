# TransformationDocumentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | 
**assembly_chart_writeoff** | **bool** |  | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**document_id** | **str** | Document identifier (GUID) | 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[TransformationDocumentCreateItem]**](TransformationDocumentCreateItem.md) | List of document items | 
**number** | **str** | Document number | 
**organization_id** | **str** | Organization identifier (GUID) | 
**product** | **str** | Product identifier (GUID) | 
**store_from** | **str** | Write-off store identifier (GUID) | 
**store_to** | **str** | Receipt store identifier (GUID) | 

## Example

```python
from iikocloud_client.models.transformation_document_update_request import TransformationDocumentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransformationDocumentUpdateRequest from a JSON string
transformation_document_update_request_instance = TransformationDocumentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TransformationDocumentUpdateRequest.to_json())

# convert the object into a dict
transformation_document_update_request_dict = transformation_document_update_request_instance.to_dict()
# create an instance of TransformationDocumentUpdateRequest from a dict
transformation_document_update_request_from_dict = TransformationDocumentUpdateRequest.from_dict(transformation_document_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


