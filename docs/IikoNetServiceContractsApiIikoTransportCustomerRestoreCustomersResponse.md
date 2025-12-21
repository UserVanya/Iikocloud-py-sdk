# IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse

Restore customers response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of unique customer IDs. | [optional] 
**restored** | **int** | Number of restored customers. | [optional] 
**not_found** | **int** | Number of unfound customers. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_response import IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_response_instance = IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_response_dict = iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse from a dict
iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_response_from_dict = IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


