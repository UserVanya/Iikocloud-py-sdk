# IikoNetServiceContractsApiIikoTransportCustomerGuestCardInfo

Guest card info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Card id. | [optional] 
**track** | **str** | Card track. | [optional] 
**number** | **str** | Card number. | [optional] 
**valid_to_date** | **str** | Card valid to date. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_guest_card_info import IikoNetServiceContractsApiIikoTransportCustomerGuestCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGuestCardInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_guest_card_info_instance = IikoNetServiceContractsApiIikoTransportCustomerGuestCardInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerGuestCardInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_guest_card_info_dict = iiko_net_service_contracts_api_iiko_transport_customer_guest_card_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGuestCardInfo from a dict
iiko_net_service_contracts_api_iiko_transport_customer_guest_card_info_from_dict = IikoNetServiceContractsApiIikoTransportCustomerGuestCardInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_guest_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


