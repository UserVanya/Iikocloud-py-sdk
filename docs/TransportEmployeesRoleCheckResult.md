# TransportEmployeesRoleCheckResult

Result of checking employee role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_role_code** | **str** | Checked for employee role. | 
**employee_has_role** | **bool** | Sign that employee has role \&quot;checkedRoleCode\&quot;. | 

## Example

```python
from iiko_cloud_client.models.transport_employees_role_check_result import TransportEmployeesRoleCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesRoleCheckResult from a JSON string
transport_employees_role_check_result_instance = TransportEmployeesRoleCheckResult.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesRoleCheckResult.to_json())

# convert the object into a dict
transport_employees_role_check_result_dict = transport_employees_role_check_result_instance.to_dict()
# create an instance of TransportEmployeesRoleCheckResult from a dict
transport_employees_role_check_result_from_dict = TransportEmployeesRoleCheckResult.from_dict(transport_employees_role_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


