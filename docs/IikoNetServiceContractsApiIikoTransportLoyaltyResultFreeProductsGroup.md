# IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_action_id** | **UUID** | Id of action that caused the suggestion. | [optional] 
**description_for_user** | **str** | Description for user. Can be null. | [optional] 
**products** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct.md) | Products that should be added to order. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_products_group import IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_products_group_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_products_group_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_products_group_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_products_group_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_products_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


