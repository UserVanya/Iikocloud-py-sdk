# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo

Combo in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Combo ID.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid(). | 
**name** | **str** | Name of combo. | 
**amount** | **int** | Quantity. | 
**price** | **float** | Price of one combo. | 
**source_id** | **UUID** | Combo validity ID. | 
**program_id** | **UUID** | Card program ID.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**size_id** | **UUID** | Size ID. Required if combo has a size scale.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_combo import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_combo_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_combo_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_combo_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_combo_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


