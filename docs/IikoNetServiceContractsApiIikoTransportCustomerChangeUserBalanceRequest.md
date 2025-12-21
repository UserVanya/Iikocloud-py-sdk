# IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest

Change user balance request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | [optional] 
**wallet_id** | **UUID** | Wallet id. | [optional] 
**sum** | **float** | Sum of balance change. Must be possible. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request import IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request_instance = IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


