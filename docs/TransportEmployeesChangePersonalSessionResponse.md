# TransportEmployeesChangePersonalSessionResponse

Personal session change response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**error** | **str** | Error details. | [optional] 

## Example

```python
from iikocloud_client.models.transport_employees_change_personal_session_response import TransportEmployeesChangePersonalSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesChangePersonalSessionResponse from a JSON string
transport_employees_change_personal_session_response_instance = TransportEmployeesChangePersonalSessionResponse.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesChangePersonalSessionResponse.to_json())

# convert the object into a dict
transport_employees_change_personal_session_response_dict = transport_employees_change_personal_session_response_instance.to_dict()
# create an instance of TransportEmployeesChangePersonalSessionResponse from a dict
transport_employees_change_personal_session_response_from_dict = TransportEmployeesChangePersonalSessionResponse.from_dict(transport_employees_change_personal_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


