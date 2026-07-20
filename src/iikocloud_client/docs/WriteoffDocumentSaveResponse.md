# WriteoffDocumentSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.writeoff_document_save_response import WriteoffDocumentSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WriteoffDocumentSaveResponse from a JSON string
writeoff_document_save_response_instance = WriteoffDocumentSaveResponse.from_json(json)
# print the JSON string representation of the object
print(WriteoffDocumentSaveResponse.to_json())

# convert the object into a dict
writeoff_document_save_response_dict = writeoff_document_save_response_instance.to_dict()
# create an instance of WriteoffDocumentSaveResponse from a dict
writeoff_document_save_response_from_dict = WriteoffDocumentSaveResponse.from_dict(writeoff_document_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


