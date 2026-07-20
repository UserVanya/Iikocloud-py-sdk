# DisassembleDocumentCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**document_id** | **str** |  | [optional] 
**items** | [**List[DisassembleDocumentCreateItem]**](DisassembleDocumentCreateItem.md) | List of document items | 
**number** | **str** | Document number | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | 
**product** | **str** | Product identifier (GUID) | 
**store_from** | **str** | Write-off store identifier (GUID) | 
**store_to** | **str** | Receipt store identifier (GUID) | 

## Example

```python
from iikocloud_client.models.disassemble_document_create_request import DisassembleDocumentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisassembleDocumentCreateRequest from a JSON string
disassemble_document_create_request_instance = DisassembleDocumentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DisassembleDocumentCreateRequest.to_json())

# convert the object into a dict
disassemble_document_create_request_dict = disassemble_document_create_request_instance.to_dict()
# create an instance of DisassembleDocumentCreateRequest from a dict
disassemble_document_create_request_from_dict = DisassembleDocumentCreateRequest.from_dict(disassemble_document_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


