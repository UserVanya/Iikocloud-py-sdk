# EmployeeWithCheckedRole

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_roles_result** | [**List[RoleCheckResult]**](RoleCheckResult.md) | Result of check employee&#39;s roles. | [optional] 
**code** | **str** | Code. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**first_name** | **str** | Name of user. | [optional] 
**id** | **UUID** | Employee ID. | 
**is_deleted** | **bool** | User deletion flag. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**middle_name** | **str** | Second name. | [optional] 

## Example

```python
from iikocloud_client.models.employee_with_checked_role import EmployeeWithCheckedRole

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeWithCheckedRole from a JSON string
employee_with_checked_role_instance = EmployeeWithCheckedRole.from_json(json)
# print the JSON string representation of the object
print(EmployeeWithCheckedRole.to_json())

# convert the object into a dict
employee_with_checked_role_dict = employee_with_checked_role_instance.to_dict()
# create an instance of EmployeeWithCheckedRole from a dict
employee_with_checked_role_from_dict = EmployeeWithCheckedRole.from_dict(employee_with_checked_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


