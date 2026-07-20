# DisassembleDocumentListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**conception** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**document_id** | **str** |  | [optional] 
**is_editable** | **bool** |  | [optional] 
**number** | **str** |  | [optional] 
**processed** | **bool** |  | [optional] 
**store_from** | **str** |  | [optional] 
**store_to** | **str** |  | [optional] 
**sum** | **float** |  | [optional] 
**sum_without_vat** | **float** |  | [optional] 
**user_created** | **str** |  | [optional] 
**user_modified** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.disassemble_document_list_item import DisassembleDocumentListItem

# TODO update the JSON string below
json = "{}"
# create an instance of DisassembleDocumentListItem from a JSON string
disassemble_document_list_item_instance = DisassembleDocumentListItem.from_json(json)
# print the JSON string representation of the object
print(DisassembleDocumentListItem.to_json())

# convert the object into a dict
disassemble_document_list_item_dict = disassemble_document_list_item_instance.to_dict()
# create an instance of DisassembleDocumentListItem from a dict
disassemble_document_list_item_from_dict = DisassembleDocumentListItem.from_dict(disassemble_document_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


