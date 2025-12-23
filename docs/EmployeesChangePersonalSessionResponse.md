# EmployeesChangePersonalSessionResponse

Personal session change response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**error** | **str** | Error details. | [optional] 

## Example

```python
from iikocloud_client.models.employees_change_personal_session_response import EmployeesChangePersonalSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesChangePersonalSessionResponse from a JSON string
employees_change_personal_session_response_instance = EmployeesChangePersonalSessionResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesChangePersonalSessionResponse.to_json())

# convert the object into a dict
employees_change_personal_session_response_dict = employees_change_personal_session_response_instance.to_dict()
# create an instance of EmployeesChangePersonalSessionResponse from a dict
employees_change_personal_session_response_from_dict = EmployeesChangePersonalSessionResponse.from_dict(employees_change_personal_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


