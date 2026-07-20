# DisassembleDocumentGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**main_product_amount_percent** | **float** |  | [optional] 
**num** | **int** | Item sequence number | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.disassemble_document_get_item import DisassembleDocumentGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of DisassembleDocumentGetItem from a JSON string
disassemble_document_get_item_instance = DisassembleDocumentGetItem.from_json(json)
# print the JSON string representation of the object
print(DisassembleDocumentGetItem.to_json())

# convert the object into a dict
disassemble_document_get_item_dict = disassemble_document_get_item_instance.to_dict()
# create an instance of DisassembleDocumentGetItem from a dict
disassemble_document_get_item_from_dict = DisassembleDocumentGetItem.from_dict(disassemble_document_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


