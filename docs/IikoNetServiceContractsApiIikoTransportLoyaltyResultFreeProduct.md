# IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id of product. | [optional] 
**code** | **str** | Code of product. Can be null. | [optional] 
**size** | **List[str]** | Sizes available for that product. | [optional] 
**sizes** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductSize]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductSize.md) | Sizes with IDs available for that product. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_product import IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_product_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_product_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_product_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_product_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProduct.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_free_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


