# IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount

Manual discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_condition_id** | **UUID** | Manual discount condition identifier. | [optional] 
**sum** | **float** | Discount amount. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_dynamic_discount import IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_dynamic_discount_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_dynamic_discount_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_dynamic_discount_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_dynamic_discount_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


