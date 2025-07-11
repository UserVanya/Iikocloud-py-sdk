# TransportEmployeesEmployeesWithRoleSignResponse

Wrapping object to retrieve list of drivers from iikoRMS with checked role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**employees_with_check_roles** | [**List[TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole]**](TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole.md) | List of drivers. | 

## Example

```python
from iikocloud_client.models.transport_employees_employees_with_role_sign_response import TransportEmployeesEmployeesWithRoleSignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesEmployeesWithRoleSignResponse from a JSON string
transport_employees_employees_with_role_sign_response_instance = TransportEmployeesEmployeesWithRoleSignResponse.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesEmployeesWithRoleSignResponse.to_json())

# convert the object into a dict
transport_employees_employees_with_role_sign_response_dict = transport_employees_employees_with_role_sign_response_instance.to_dict()
# create an instance of TransportEmployeesEmployeesWithRoleSignResponse from a dict
transport_employees_employees_with_role_sign_response_from_dict = TransportEmployeesEmployeesWithRoleSignResponse.from_dict(transport_employees_employees_with_role_sign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


