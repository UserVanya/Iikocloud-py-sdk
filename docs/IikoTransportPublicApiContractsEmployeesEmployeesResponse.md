# IikoTransportPublicApiContractsEmployeesEmployeesResponse

Wrapping object to retrieve list of drivers from iikoRMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**employees** | [**List[RmsItemsResponseWrapperEmployeesEmployee]**](RmsItemsResponseWrapperEmployeesEmployee.md) | List of drivers. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employees_response import IikoTransportPublicApiContractsEmployeesEmployeesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeesResponse from a JSON string
iiko_transport_public_api_contracts_employees_employees_response_instance = IikoTransportPublicApiContractsEmployeesEmployeesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesEmployeesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_employees_response_dict = iiko_transport_public_api_contracts_employees_employees_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeesResponse from a dict
iiko_transport_public_api_contracts_employees_employees_response_from_dict = IikoTransportPublicApiContractsEmployeesEmployeesResponse.from_dict(iiko_transport_public_api_contracts_employees_employees_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


