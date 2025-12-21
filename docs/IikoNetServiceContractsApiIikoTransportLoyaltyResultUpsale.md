# IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale

user tip.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_action_id** | **UUID** | Id of action that caused the suggestion. | [optional] 
**suggestion_text** | **str** | Suggestion text. | [optional] 
**description_for_user** | **str** | Description for user. | [optional] 
**product_codes** | **List[str]** | Codes of products that suggested to be added to order. | [optional] 
**products** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsaleProduct]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsaleProduct.md) | Products that suggested to be added to order. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_upsale import IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_upsale_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_upsale_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_upsale_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_upsale_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_upsale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


