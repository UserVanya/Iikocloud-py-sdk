# IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_component** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent**](IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent.md) | Main component. | 
**secondary_component** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent**](IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent.md) | Additional component. | [optional] 
**common_modifiers** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemModifier]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemModifier.md) | Indivisible modifiers. | [optional] 
**template** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundItemTemplate**](IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundItemTemplate.md) | Modifier scheme. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item import IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItem from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_dict = iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItem from a dict
iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItem.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


