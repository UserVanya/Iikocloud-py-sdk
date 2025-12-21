# EmployeesClosePersonalSessionRequest

Close personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**employee_id** | **UUID** | Employee ID. | 

## Example

```python
from iikocloud_client.models.employees_close_personal_session_request import EmployeesClosePersonalSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesClosePersonalSessionRequest from a JSON string
employees_close_personal_session_request_instance = EmployeesClosePersonalSessionRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeesClosePersonalSessionRequest.to_json())

# convert the object into a dict
employees_close_personal_session_request_dict = employees_close_personal_session_request_instance.to_dict()
# create an instance of EmployeesClosePersonalSessionRequest from a dict
employees_close_personal_session_request_from_dict = EmployeesClosePersonalSessionRequest.from_dict(employees_close_personal_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


