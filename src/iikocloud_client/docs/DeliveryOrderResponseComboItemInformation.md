# DeliveryOrderResponseComboItemInformation

Information on order item to combo relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_id** | **UUID** | New combo ID. | 
**combo_source_id** | **UUID** | Action ID that defines combo. | 
**group_id** | **UUID** | Combo group ID to which item belongs. | 
**group_name** | **str** | Combo group name to which item belongs. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_combo_item_information import DeliveryOrderResponseComboItemInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseComboItemInformation from a JSON string
delivery_order_response_combo_item_information_instance = DeliveryOrderResponseComboItemInformation.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseComboItemInformation.to_json())

# convert the object into a dict
delivery_order_response_combo_item_information_dict = delivery_order_response_combo_item_information_instance.to_dict()
# create an instance of DeliveryOrderResponseComboItemInformation from a dict
delivery_order_response_combo_item_information_from_dict = DeliveryOrderResponseComboItemInformation.from_dict(delivery_order_response_combo_item_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


