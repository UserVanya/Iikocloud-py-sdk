# DeliveryOrderCreateComboItemInformation

Combo details if order item belongs to combo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_group_id** | **UUID** | Combo group ID to which item belongs. | 
**combo_group_name** | **str** | Combo group name to which item belongs. | [optional] 
**combo_id** | **UUID** | Created combo ID.  Must be one of combos.id generated values. | 
**combo_source_id** | **UUID** | Action ID that defines combo. | 

## Example

```python
from iikocloud_client.models.delivery_order_create_combo_item_information import DeliveryOrderCreateComboItemInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateComboItemInformation from a JSON string
delivery_order_create_combo_item_information_instance = DeliveryOrderCreateComboItemInformation.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateComboItemInformation.to_json())

# convert the object into a dict
delivery_order_create_combo_item_information_dict = delivery_order_create_combo_item_information_instance.to_dict()
# create an instance of DeliveryOrderCreateComboItemInformation from a dict
delivery_order_create_combo_item_information_from_dict = DeliveryOrderCreateComboItemInformation.from_dict(delivery_order_create_combo_item_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


