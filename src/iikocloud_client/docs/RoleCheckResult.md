# RoleCheckResult

Result of checking employee role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_role_code** | **str** | Checked for employee role. | 
**employee_has_role** | **bool** | Sign that employee has role \&quot;checkedRoleCode\&quot;. | 

## Example

```python
from iikocloud_client.models.role_check_result import RoleCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCheckResult from a JSON string
role_check_result_instance = RoleCheckResult.from_json(json)
# print the JSON string representation of the object
print(RoleCheckResult.to_json())

# convert the object into a dict
role_check_result_dict = role_check_result_instance.to_dict()
# create an instance of RoleCheckResult from a dict
role_check_result_from_dict = RoleCheckResult.from_dict(role_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


