# EmployeesRoleCheckResult

Result of checking employee role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_role_code** | **str** | Checked for employee role. | 
**employee_has_role** | **bool** | Sign that employee has role \&quot;checkedRoleCode\&quot;. | 

## Example

```python
from iikocloud_client.models.employees_role_check_result import EmployeesRoleCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesRoleCheckResult from a JSON string
employees_role_check_result_instance = EmployeesRoleCheckResult.from_json(json)
# print the JSON string representation of the object
print(EmployeesRoleCheckResult.to_json())

# convert the object into a dict
employees_role_check_result_dict = employees_role_check_result_instance.to_dict()
# create an instance of EmployeesRoleCheckResult from a dict
employees_role_check_result_from_dict = EmployeesRoleCheckResult.from_dict(employees_role_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


