# IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Product ID. | 
**product** | **str** | Product. | 
**amount** | **float** | Amount. | 
**modifiers** | [**List[IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier]**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier.md) | Modifiers (absolute amount). | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_order_item import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_order_item_instance = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_order_item_dict = iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_order_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem from a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_order_item_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


