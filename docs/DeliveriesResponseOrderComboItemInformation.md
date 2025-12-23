# DeliveriesResponseOrderComboItemInformation

Information on order item to combo relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_id** | **str** | New combo ID. | 
**combo_source_id** | **str** | Action ID that defines combo. | 
**group_id** | **str** | Combo group ID to which item belongs. | 
**group_name** | **str** | Combo group name to which item belongs. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_combo_item_information import DeliveriesResponseOrderComboItemInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderComboItemInformation from a JSON string
deliveries_response_order_combo_item_information_instance = DeliveriesResponseOrderComboItemInformation.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderComboItemInformation.to_json())

# convert the object into a dict
deliveries_response_order_combo_item_information_dict = deliveries_response_order_combo_item_information_instance.to_dict()
# create an instance of DeliveriesResponseOrderComboItemInformation from a dict
deliveries_response_order_combo_item_information_from_dict = DeliveriesResponseOrderComboItemInformation.from_dict(deliveries_response_order_combo_item_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


