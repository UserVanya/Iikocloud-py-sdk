# IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest

Base class for customer info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**organization_id** | **UUID** | Organization id. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request import IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request_instance = IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


