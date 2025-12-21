# IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent

Part of composite item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderProduct**](IikoTransportPublicApiContractsDeliveriesResponseOrderProduct.md) | Item. | 
**modifiers** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemModifier]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**cost** | **float** | Item total including tax, discounts/surcharges. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**position_id** | **UUID** | Unique identifier of the item in the order and for the whole system. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_component import IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_component_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_component_dict = iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_component_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent from a dict
iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_component_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderCompoundOrderItemComponent.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_compound_order_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


