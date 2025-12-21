# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount

Dynamic discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_condition_id** | **UUID** | Applied manual condition ID. | 
**sum** | **float** | Discount sum. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_dynamic_discount import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_dynamic_discount_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_dynamic_discount_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_dynamic_discount_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_dynamic_discount_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


