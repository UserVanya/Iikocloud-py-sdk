# WriteoffDocumentListItem


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
**expense_account** | **str** |  | [optional] 
**is_editable** | **bool** |  | [optional] 
**number** | **str** |  | [optional] 
**processed** | **bool** |  | [optional] 
**store_from** | **str** |  | [optional] 
**sum** | **float** |  | [optional] 
**sum_without_vat** | **float** |  | [optional] 
**user_created** | **str** |  | [optional] 
**user_modified** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.writeoff_document_list_item import WriteoffDocumentListItem

# TODO update the JSON string below
json = "{}"
# create an instance of WriteoffDocumentListItem from a JSON string
writeoff_document_list_item_instance = WriteoffDocumentListItem.from_json(json)
# print the JSON string representation of the object
print(WriteoffDocumentListItem.to_json())

# convert the object into a dict
writeoff_document_list_item_dict = writeoff_document_list_item_instance.to_dict()
# create an instance of WriteoffDocumentListItem from a dict
writeoff_document_list_item_from_dict = WriteoffDocumentListItem.from_dict(writeoff_document_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


