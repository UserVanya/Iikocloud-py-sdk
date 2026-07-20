# DisassembleDocumentCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**main_product_amount_percent** | **float** |  | 
**num** | **int** | Item sequence number | 
**product** | **str** | Product identifier (GUID) | 

## Example

```python
from iikocloud_client.models.disassemble_document_create_item import DisassembleDocumentCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of DisassembleDocumentCreateItem from a JSON string
disassemble_document_create_item_instance = DisassembleDocumentCreateItem.from_json(json)
# print the JSON string representation of the object
print(DisassembleDocumentCreateItem.to_json())

# convert the object into a dict
disassemble_document_create_item_dict = disassemble_document_create_item_instance.to_dict()
# create an instance of DisassembleDocumentCreateItem from a dict
disassemble_document_create_item_from_dict = DisassembleDocumentCreateItem.from_dict(disassemble_document_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


