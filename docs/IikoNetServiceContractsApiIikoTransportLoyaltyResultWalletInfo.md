# IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo

Wallet info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Wallet id. | [optional] 
**max_sum** | **float** | Max sum for payment from the wallet. | [optional] 
**can_hold_money** | **bool** | Can hold money. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_wallet_info import IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_wallet_info_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_wallet_info_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_wallet_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_wallet_info_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


