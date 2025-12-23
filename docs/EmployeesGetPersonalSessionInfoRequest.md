# EmployeesGetPersonalSessionInfoRequest

Personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Delivery group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**employee_id** | **str** | Employee ID. | 

## Example

```python
from iikocloud_client.models.employees_get_personal_session_info_request import EmployeesGetPersonalSessionInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesGetPersonalSessionInfoRequest from a JSON string
employees_get_personal_session_info_request_instance = EmployeesGetPersonalSessionInfoRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeesGetPersonalSessionInfoRequest.to_json())

# convert the object into a dict
employees_get_personal_session_info_request_dict = employees_get_personal_session_info_request_instance.to_dict()
# create an instance of EmployeesGetPersonalSessionInfoRequest from a dict
employees_get_personal_session_info_request_from_dict = EmployeesGetPersonalSessionInfoRequest.from_dict(employees_get_personal_session_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


