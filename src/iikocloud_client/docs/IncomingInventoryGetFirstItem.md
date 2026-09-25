# IncomingInventoryGetFirstItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**comment** | **str** | Comment | [optional] 
**num** | **int** | Item sequence number | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**product_size** | **str** | Product size identifier (GUID) | [optional] 
**turnover** | **float** | Product turnover for the period. Read-only. Can be null | [optional] 

## Example

```python
from iikocloud_client.models.incoming_inventory_get_first_item import IncomingInventoryGetFirstItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventoryGetFirstItem from a JSON string
incoming_inventory_get_first_item_instance = IncomingInventoryGetFirstItem.from_json(json)
# print the JSON string representation of the object
print(IncomingInventoryGetFirstItem.to_json())

# convert the object into a dict
incoming_inventory_get_first_item_dict = incoming_inventory_get_first_item_instance.to_dict()
# create an instance of IncomingInventoryGetFirstItem from a dict
incoming_inventory_get_first_item_from_dict = IncomingInventoryGetFirstItem.from_dict(incoming_inventory_get_first_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


