# DisassembleDocumentSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.disassemble_document_save_response import DisassembleDocumentSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisassembleDocumentSaveResponse from a JSON string
disassemble_document_save_response_instance = DisassembleDocumentSaveResponse.from_json(json)
# print the JSON string representation of the object
print(DisassembleDocumentSaveResponse.to_json())

# convert the object into a dict
disassemble_document_save_response_dict = disassemble_document_save_response_instance.to_dict()
# create an instance of DisassembleDocumentSaveResponse from a dict
disassemble_document_save_response_from_dict = DisassembleDocumentSaveResponse.from_dict(disassemble_document_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


