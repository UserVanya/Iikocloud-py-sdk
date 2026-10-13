# TransformationDocumentListItem


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
**items** | [**List[TransformationDocumentGetItem]**](TransformationDocumentGetItem.md) | List of document items | [optional] 
**number** | **str** |  | [optional] 
**processed** | **bool** |  | [optional] 
**revision** | **int** | Document revision — a monotonically increasing version number that grows on every change. In the list response it appears only when changed documents (revision) or full details (returnFullDetails) are requested | [optional] 
**store_from** | **str** |  | [optional] 
**store_to** | **str** |  | [optional] 
**sum** | **float** |  | [optional] 
**sum_without_vat** | **float** |  | [optional] 
**user_created** | **str** |  | [optional] 
**user_modified** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.transformation_document_list_item import TransformationDocumentListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransformationDocumentListItem from a JSON string
transformation_document_list_item_instance = TransformationDocumentListItem.from_json(json)
# print the JSON string representation of the object
print(TransformationDocumentListItem.to_json())

# convert the object into a dict
transformation_document_list_item_dict = transformation_document_list_item_instance.to_dict()
# create an instance of TransformationDocumentListItem from a dict
transformation_document_list_item_from_dict = TransformationDocumentListItem.from_dict(transformation_document_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


