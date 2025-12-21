# IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest

Cancel hold money request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **UUID** | Transaction id. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request import IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request_instance = IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


