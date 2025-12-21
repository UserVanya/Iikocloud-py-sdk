# IikoTransportPublicApiContractsDeliveriesResponseOrderDynamicDiscount

Dynamic discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_condition_id** | **UUID** | Applied manual condition ID. | 
**sum** | **float** | Discount sum. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_dynamic_discount import IikoTransportPublicApiContractsDeliveriesResponseOrderDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderDynamicDiscount from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_dynamic_discount_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderDynamicDiscount.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_dynamic_discount_dict = iiko_transport_public_api_contracts_deliveries_response_order_dynamic_discount_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderDynamicDiscount from a dict
iiko_transport_public_api_contracts_deliveries_response_order_dynamic_discount_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderDynamicDiscount.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


