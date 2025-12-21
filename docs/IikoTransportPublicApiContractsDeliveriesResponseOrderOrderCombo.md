# IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo

Combo in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Combo ID. | 
**name** | **str** | Name of combo. | 
**amount** | **int** | Number of combos. | 
**price** | **float** | Price of combo. Given for 1 combo, without regard to amount. | 
**source_id** | **UUID** | Combo action ID. | 
**size** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderProductSize**](IikoTransportPublicApiContractsDeliveriesResponseOrderProductSize.md) | Size. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_order_combo import IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_order_combo_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_combo_dict = iiko_transport_public_api_contracts_deliveries_response_order_order_combo_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo from a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_combo_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_order_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


