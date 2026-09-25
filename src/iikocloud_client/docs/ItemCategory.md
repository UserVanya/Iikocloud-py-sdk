# ItemCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Fiscal category code | [optional] 
**id** | **UUID** | Fiscal category UUID. string (UUID) | [optional] 
**is_deleted** | **bool** | Deleted flag | [optional] 
**name** | **str** | Display name | [optional] 

## Example

```python
from iikocloud_client.models.item_category import ItemCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCategory from a JSON string
item_category_instance = ItemCategory.from_json(json)
# print the JSON string representation of the object
print(ItemCategory.to_json())

# convert the object into a dict
item_category_dict = item_category_instance.to_dict()
# create an instance of ItemCategory from a dict
item_category_from_dict = ItemCategory.from_dict(item_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


