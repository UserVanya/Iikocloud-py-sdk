# IikoNetServiceContractsApiIikoTransportCustomerGuestBalanceInfo

Information about guest balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Wallet id. | [optional] 
**name** | **str** | Wallet name. | [optional] 
**type** | [**IikoNetServiceContractsApiIikoTransportProgramType**](IikoNetServiceContractsApiIikoTransportProgramType.md) | Wallet type.  &lt;br&gt;0 - deposit or corporate nutrition,&lt;br /&gt;1 - bonus program,&lt;br /&gt;2 - products program,&lt;br /&gt;3 - discount program,&lt;br /&gt;4 - certificate program. | [optional] 
**balance** | **float** | Wallet balance. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_guest_balance_info import IikoNetServiceContractsApiIikoTransportCustomerGuestBalanceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGuestBalanceInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_guest_balance_info_instance = IikoNetServiceContractsApiIikoTransportCustomerGuestBalanceInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerGuestBalanceInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_guest_balance_info_dict = iiko_net_service_contracts_api_iiko_transport_customer_guest_balance_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGuestBalanceInfo from a dict
iiko_net_service_contracts_api_iiko_transport_customer_guest_balance_info_from_dict = IikoNetServiceContractsApiIikoTransportCustomerGuestBalanceInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_guest_balance_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


