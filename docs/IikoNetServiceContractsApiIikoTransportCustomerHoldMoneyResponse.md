# IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse

Hold money response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **UUID** | Holding money transaction id. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_hold_money_response import IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_hold_money_response_instance = IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_hold_money_response_dict = iiko_net_service_contracts_api_iiko_transport_customer_hold_money_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse from a dict
iiko_net_service_contracts_api_iiko_transport_customer_hold_money_response_from_dict = IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_hold_money_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


