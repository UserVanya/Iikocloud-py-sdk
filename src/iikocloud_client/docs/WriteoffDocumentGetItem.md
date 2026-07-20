# WriteoffDocumentGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_factor** | **float** | Write-off factor | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**num** | **int** | Item sequence number | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**product_size** | **str** | Product size identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.writeoff_document_get_item import WriteoffDocumentGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of WriteoffDocumentGetItem from a JSON string
writeoff_document_get_item_instance = WriteoffDocumentGetItem.from_json(json)
# print the JSON string representation of the object
print(WriteoffDocumentGetItem.to_json())

# convert the object into a dict
writeoff_document_get_item_dict = writeoff_document_get_item_instance.to_dict()
# create an instance of WriteoffDocumentGetItem from a dict
writeoff_document_get_item_from_dict = WriteoffDocumentGetItem.from_dict(writeoff_document_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


