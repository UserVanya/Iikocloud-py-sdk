# IikoTransportPublicApiContractsEmployeesCouriersRequest

Request for list of drivers for organizations in OrganizationIds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | List of organizations. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_couriers_request import IikoTransportPublicApiContractsEmployeesCouriersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesCouriersRequest from a JSON string
iiko_transport_public_api_contracts_employees_couriers_request_instance = IikoTransportPublicApiContractsEmployeesCouriersRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesCouriersRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_couriers_request_dict = iiko_transport_public_api_contracts_employees_couriers_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesCouriersRequest from a dict
iiko_transport_public_api_contracts_employees_couriers_request_from_dict = IikoTransportPublicApiContractsEmployeesCouriersRequest.from_dict(iiko_transport_public_api_contracts_employees_couriers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


