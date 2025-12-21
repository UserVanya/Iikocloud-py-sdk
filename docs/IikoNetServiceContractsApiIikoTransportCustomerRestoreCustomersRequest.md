# IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest

Restore customers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[UUID]** | Customer IDs to recover. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request import IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request_instance = IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


