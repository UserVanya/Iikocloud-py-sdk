# IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest

Add customer to program request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | [optional] 
**program_id** | **UUID** | Program id. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request import IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request_instance = IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


