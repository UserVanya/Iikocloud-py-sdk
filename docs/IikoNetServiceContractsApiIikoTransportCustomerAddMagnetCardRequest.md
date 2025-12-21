# IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest

Add magnet card request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**card_track** | **str** | Card track. Can be null. | 
**card_number** | **str** | Card number. Can be null. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request import IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request_instance = IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


