# IncomingInventoryCreateFirstStepItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**comment** | **str** | Comment | [optional] 
**num** | **int** | Item sequence number | 
**product** | **str** | Product identifier (GUID) | 
**product_size** | **str** | Product size identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_inventory_create_first_step_item import IncomingInventoryCreateFirstStepItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventoryCreateFirstStepItem from a JSON string
incoming_inventory_create_first_step_item_instance = IncomingInventoryCreateFirstStepItem.from_json(json)
# print the JSON string representation of the object
print(IncomingInventoryCreateFirstStepItem.to_json())

# convert the object into a dict
incoming_inventory_create_first_step_item_dict = incoming_inventory_create_first_step_item_instance.to_dict()
# create an instance of IncomingInventoryCreateFirstStepItem from a dict
incoming_inventory_create_first_step_item_from_dict = IncomingInventoryCreateFirstStepItem.from_dict(incoming_inventory_create_first_step_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


