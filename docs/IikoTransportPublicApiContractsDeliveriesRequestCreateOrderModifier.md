# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier

Modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Modifier item ID.                Can be obtained by &#x60;/nomenclature&#x60; operation. | 
**amount** | **float** | Quantity. | 
**product_group_id** | **UUID** | Modifiers group ID (for group modifier). Required for a group modifier.                Can be obtained by &#x60;/nomenclature&#x60; operation. | [optional] 
**price** | **float** | Unit price. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_modifier import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_modifier_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_modifier_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_modifier_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_modifier_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


