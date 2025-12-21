# IikoTransportPublicApiContractsEmployeesRoleCheckResult

Result of checking employee role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_role_code** | **str** | Checked for employee role. | 
**employee_has_role** | **bool** | Sign that employee has role \&quot;checkedRoleCode\&quot;. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_role_check_result import IikoTransportPublicApiContractsEmployeesRoleCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesRoleCheckResult from a JSON string
iiko_transport_public_api_contracts_employees_role_check_result_instance = IikoTransportPublicApiContractsEmployeesRoleCheckResult.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesRoleCheckResult.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_role_check_result_dict = iiko_transport_public_api_contracts_employees_role_check_result_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesRoleCheckResult from a dict
iiko_transport_public_api_contracts_employees_role_check_result_from_dict = IikoTransportPublicApiContractsEmployeesRoleCheckResult.from_dict(iiko_transport_public_api_contracts_employees_role_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


