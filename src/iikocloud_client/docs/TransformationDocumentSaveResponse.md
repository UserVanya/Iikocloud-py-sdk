# TransformationDocumentSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.transformation_document_save_response import TransformationDocumentSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransformationDocumentSaveResponse from a JSON string
transformation_document_save_response_instance = TransformationDocumentSaveResponse.from_json(json)
# print the JSON string representation of the object
print(TransformationDocumentSaveResponse.to_json())

# convert the object into a dict
transformation_document_save_response_dict = transformation_document_save_response_instance.to_dict()
# create an instance of TransformationDocumentSaveResponse from a dict
transformation_document_save_response_from_dict = TransformationDocumentSaveResponse.from_dict(transformation_document_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


