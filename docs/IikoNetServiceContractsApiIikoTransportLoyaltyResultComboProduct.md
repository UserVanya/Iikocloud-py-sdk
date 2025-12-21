# IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct

Combo product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Product id. | [optional] 
**size_name** | **str** | Size name. Can be null. | [optional] 
**size_id** | **UUID** | Size id. | [optional] 
**forbidden_modifiers** | **List[UUID]** | Forbidden modifiers. | [optional] 
**price_modification_amount** | **float** | Price modification amount. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_product import IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_product_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_product_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_product_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_product_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


