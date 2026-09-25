# IncomingInventoryGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**comment** | **str** | Comment | [optional] 
**container_count** | **float** | Quantity in container/package (containerId) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**container_name** | **str** | Container/package name | [optional] 
**count** | **float** | Quantity in base unit of measure | [optional] 
**count_gross** | **float** | Gross weight (with container) | [optional] 
**current_actual_amount** | **float** | Actual quantity including dishes and preparations. Read-only | [optional] 
**is_disassembled** | **bool** | Ingredient flag. true — item is an ingredient of another first-step item | [optional] 
**num** | **int** | Item sequence number | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**recalculation_date** | **str** | Recalculation date. Read-only. Can be null | [optional] 
**recalculation_number** | **int** | Recalculation sequence number. Read-only | [optional] 
**status** | **str** | Item status (NEW — unsaved, SAVE — saved, RECALC — recalculated/deleted) | [optional] 
**turnover** | **float** | Product turnover for the period. Read-only. Can be null | [optional] 

## Example

```python
from iikocloud_client.models.incoming_inventory_get_item import IncomingInventoryGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventoryGetItem from a JSON string
incoming_inventory_get_item_instance = IncomingInventoryGetItem.from_json(json)
# print the JSON string representation of the object
print(IncomingInventoryGetItem.to_json())

# convert the object into a dict
incoming_inventory_get_item_dict = incoming_inventory_get_item_instance.to_dict()
# create an instance of IncomingInventoryGetItem from a dict
incoming_inventory_get_item_from_dict = IncomingInventoryGetItem.from_dict(incoming_inventory_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


