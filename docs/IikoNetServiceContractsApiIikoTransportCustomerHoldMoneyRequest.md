# IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest

Hold money request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **UUID** | Predefined transaction id. Random if empty. | [optional] 
**customer_id** | **UUID** | Customer id. | 
**wallet_id** | **UUID** | Wallet id. | 
**sum** | **float** | Sum. | 
**comment** | **str** | Additional information about holding. Can be null. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request import IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request_instance = IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


