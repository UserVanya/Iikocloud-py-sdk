# IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment

Available payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Marketing campaign id. | [optional] 
**max_sum** | **float** | Max sum. | [optional] 
**order** | **int** | Payment order. In case of partial payment, payments with lesser order should be filled first. | [optional] 
**wallet_infos** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultWalletInfo.md) | Wallet infos. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_payment import IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_payment_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_payment_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_payment_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_payment_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


