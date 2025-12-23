# EmployeesGetPersonalSessionInfoResponse

Personal session info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**is_session_opened** | **bool** | Is personal session opened. | [optional] 
**error** | **str** | Error details. | [optional] 

## Example

```python
from iikocloud_client.models.employees_get_personal_session_info_response import EmployeesGetPersonalSessionInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesGetPersonalSessionInfoResponse from a JSON string
employees_get_personal_session_info_response_instance = EmployeesGetPersonalSessionInfoResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesGetPersonalSessionInfoResponse.to_json())

# convert the object into a dict
employees_get_personal_session_info_response_dict = employees_get_personal_session_info_response_instance.to_dict()
# create an instance of EmployeesGetPersonalSessionInfoResponse from a dict
employees_get_personal_session_info_response_from_dict = EmployeesGetPersonalSessionInfoResponse.from_dict(employees_get_personal_session_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


