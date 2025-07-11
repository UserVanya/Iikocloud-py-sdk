# TransportDeliveriesResponseOrderOrderCombo

Combo in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Combo ID. | 
**name** | **str** | Name of combo. | 
**amount** | **int** | Number of combos. | 
**price** | **float** | Price of combo. Given for 1 combo, without regard to amount. | 
**source_id** | **str** | Combo action ID. | 
**size** | [**TransportDeliveriesResponseOrderProductSize**](TransportDeliveriesResponseOrderProductSize.md) | Size. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_order_combo import TransportDeliveriesResponseOrderOrderCombo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderOrderCombo from a JSON string
transport_deliveries_response_order_order_combo_instance = TransportDeliveriesResponseOrderOrderCombo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderOrderCombo.to_json())

# convert the object into a dict
transport_deliveries_response_order_order_combo_dict = transport_deliveries_response_order_order_combo_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderOrderCombo from a dict
transport_deliveries_response_order_order_combo_from_dict = TransportDeliveriesResponseOrderOrderCombo.from_dict(transport_deliveries_response_order_order_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


