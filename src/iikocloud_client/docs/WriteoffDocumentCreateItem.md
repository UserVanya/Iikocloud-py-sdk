# WriteoffDocumentCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**num** | **int** | Item sequence number | 
**product** | **str** | Product identifier (GUID) | 
**product_size** | **str** | Product size identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.writeoff_document_create_item import WriteoffDocumentCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of WriteoffDocumentCreateItem from a JSON string
writeoff_document_create_item_instance = WriteoffDocumentCreateItem.from_json(json)
# print the JSON string representation of the object
print(WriteoffDocumentCreateItem.to_json())

# convert the object into a dict
writeoff_document_create_item_dict = writeoff_document_create_item_instance.to_dict()
# create an instance of WriteoffDocumentCreateItem from a dict
writeoff_document_create_item_from_dict = WriteoffDocumentCreateItem.from_dict(writeoff_document_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


