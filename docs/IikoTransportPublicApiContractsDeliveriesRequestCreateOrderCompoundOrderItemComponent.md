# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent

Item component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Item ID. | 
**modifiers** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_component import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_component_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_component_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_component_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_component_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


