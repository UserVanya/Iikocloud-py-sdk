# ItemDeletedInfo

Order cancellation details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_method** | [**DeletionMethod**](DeletionMethod.md) | Deletion method. | 

## Example

```python
from iikocloud_client.models.item_deleted_info import ItemDeletedInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDeletedInfo from a JSON string
item_deleted_info_instance = ItemDeletedInfo.from_json(json)
# print the JSON string representation of the object
print(ItemDeletedInfo.to_json())

# convert the object into a dict
item_deleted_info_dict = item_deleted_info_instance.to_dict()
# create an instance of ItemDeletedInfo from a dict
item_deleted_info_from_dict = ItemDeletedInfo.from_dict(item_deleted_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


