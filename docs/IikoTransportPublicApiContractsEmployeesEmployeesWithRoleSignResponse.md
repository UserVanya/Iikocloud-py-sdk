# IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse

Wrapping object to retrieve list of drivers from iikoRMS with checked role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**employees_with_check_roles** | [**List[RmsItemsResponseWrapperEmployeesEmployeeWithCheckedRole]**](RmsItemsResponseWrapperEmployeesEmployeeWithCheckedRole.md) | List of drivers. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employees_with_role_sign_response import IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse from a JSON string
iiko_transport_public_api_contracts_employees_employees_with_role_sign_response_instance = IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_employees_with_role_sign_response_dict = iiko_transport_public_api_contracts_employees_employees_with_role_sign_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse from a dict
iiko_transport_public_api_contracts_employees_employees_with_role_sign_response_from_dict = IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse.from_dict(iiko_transport_public_api_contracts_employees_employees_with_role_sign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


