# InventoryConception


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User-defined conception code | [optional] 
**id** | **str** | Conception identifier (UUID) | [optional] 
**is_deleted** | **bool** | Flag indicating that the conception is logically deleted | [optional] 
**name** | **str** | Display name of the conception | [optional] 

## Example

```python
from iikocloud_client.models.inventory_conception import InventoryConception

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryConception from a JSON string
inventory_conception_instance = InventoryConception.from_json(json)
# print the JSON string representation of the object
print(InventoryConception.to_json())

# convert the object into a dict
inventory_conception_dict = inventory_conception_instance.to_dict()
# create an instance of InventoryConception from a dict
inventory_conception_from_dict = InventoryConception.from_dict(inventory_conception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


