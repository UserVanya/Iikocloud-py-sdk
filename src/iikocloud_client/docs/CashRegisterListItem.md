# CashRegisterListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Cash register identifier (UUID) | [optional] 
**name** | **str** | Cash register name | [optional] 
**number** | **str** | Cash register number | [optional] 
**status** | **str** | Cash register status | [optional] 
**terminal_group_ids** | **List[UUID]** | Identifiers of the terminal groups linked to the cash register (UUID) | [optional] 

## Example

```python
from iikocloud_client.models.cash_register_list_item import CashRegisterListItem

# TODO update the JSON string below
json = "{}"
# create an instance of CashRegisterListItem from a JSON string
cash_register_list_item_instance = CashRegisterListItem.from_json(json)
# print the JSON string representation of the object
print(CashRegisterListItem.to_json())

# convert the object into a dict
cash_register_list_item_dict = cash_register_list_item_instance.to_dict()
# create an instance of CashRegisterListItem from a dict
cash_register_list_item_from_dict = CashRegisterListItem.from_dict(cash_register_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


