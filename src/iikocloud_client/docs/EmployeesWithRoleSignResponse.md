# EmployeesWithRoleSignResponse

Wrapping object to retrieve list of drivers from iikoRMS with checked role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**employees_with_check_roles** | [**List[RmsEmployeeWithCheckedRoleItemsResponse]**](RmsEmployeeWithCheckedRoleItemsResponse.md) | List of drivers. | 

## Example

```python
from iikocloud_client.models.employees_with_role_sign_response import EmployeesWithRoleSignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesWithRoleSignResponse from a JSON string
employees_with_role_sign_response_instance = EmployeesWithRoleSignResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesWithRoleSignResponse.to_json())

# convert the object into a dict
employees_with_role_sign_response_dict = employees_with_role_sign_response_instance.to_dict()
# create an instance of EmployeesWithRoleSignResponse from a dict
employees_with_role_sign_response_from_dict = EmployeesWithRoleSignResponse.from_dict(employees_with_role_sign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


