# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_component** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent.md) | Main component. | 
**secondary_component** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItemComponent.md) | Minor component. | [optional] 
**common_modifiers** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderModifier.md) | Indivisible modifiers. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItem from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItem from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCompoundOrderItem.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_compound_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


