# IncomingInventoryCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**comment** | **str** | Comment | [optional] 
**container_count** | **float** | Quantity in container/package (containerId) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**is_disassembled** | **bool** | Ingredient flag. true — item is an ingredient of another first-step item | [optional] 
**num** | **int** | Item sequence number | 
**product** | **str** | Product identifier (GUID) | 

## Example

```python
from iikocloud_client.models.incoming_inventory_create_item import IncomingInventoryCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventoryCreateItem from a JSON string
incoming_inventory_create_item_instance = IncomingInventoryCreateItem.from_json(json)
# print the JSON string representation of the object
print(IncomingInventoryCreateItem.to_json())

# convert the object into a dict
incoming_inventory_create_item_dict = incoming_inventory_create_item_instance.to_dict()
# create an instance of IncomingInventoryCreateItem from a dict
incoming_inventory_create_item_from_dict = IncomingInventoryCreateItem.from_dict(incoming_inventory_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


