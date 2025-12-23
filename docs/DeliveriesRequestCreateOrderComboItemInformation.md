# DeliveriesRequestCreateOrderComboItemInformation

Combo details if order item belongs to combo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_id** | **str** | Created combo ID.  Must be one of combos.id generated values. | 
**combo_source_id** | **str** | Action ID that defines combo. | 
**combo_group_id** | **str** | Combo group ID to which item belongs. | 
**combo_group_name** | **str** | Combo group name to which item belongs. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_combo_item_information import DeliveriesRequestCreateOrderComboItemInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderComboItemInformation from a JSON string
deliveries_request_create_order_combo_item_information_instance = DeliveriesRequestCreateOrderComboItemInformation.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderComboItemInformation.to_json())

# convert the object into a dict
deliveries_request_create_order_combo_item_information_dict = deliveries_request_create_order_combo_item_information_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderComboItemInformation from a dict
deliveries_request_create_order_combo_item_information_from_dict = DeliveriesRequestCreateOrderComboItemInformation.from_dict(deliveries_request_create_order_combo_item_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


