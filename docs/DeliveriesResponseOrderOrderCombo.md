# DeliveriesResponseOrderOrderCombo

Combo in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Combo ID. | 
**name** | **str** | Name of combo. | 
**amount** | **int** | Number of combos. | 
**price** | **float** | Price of combo. Given for 1 combo, without regard to amount. | 
**source_id** | **str** | Combo action ID. | 
**size** | [**DeliveriesResponseOrderProductSize**](DeliveriesResponseOrderProductSize.md) | Size. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_order_combo import DeliveriesResponseOrderOrderCombo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderOrderCombo from a JSON string
deliveries_response_order_order_combo_instance = DeliveriesResponseOrderOrderCombo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderOrderCombo.to_json())

# convert the object into a dict
deliveries_response_order_order_combo_dict = deliveries_response_order_order_combo_instance.to_dict()
# create an instance of DeliveriesResponseOrderOrderCombo from a dict
deliveries_response_order_order_combo_from_dict = DeliveriesResponseOrderOrderCombo.from_dict(deliveries_response_order_order_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


