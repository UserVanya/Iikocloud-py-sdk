# TransportEmployeesGetPersonalSessionInfoResponse

Personal session info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**is_session_opened** | **bool** | Is personal session opened. | [optional] 
**error** | **str** | Error details. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_employees_get_personal_session_info_response import TransportEmployeesGetPersonalSessionInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesGetPersonalSessionInfoResponse from a JSON string
transport_employees_get_personal_session_info_response_instance = TransportEmployeesGetPersonalSessionInfoResponse.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesGetPersonalSessionInfoResponse.to_json())

# convert the object into a dict
transport_employees_get_personal_session_info_response_dict = transport_employees_get_personal_session_info_response_instance.to_dict()
# create an instance of TransportEmployeesGetPersonalSessionInfoResponse from a dict
transport_employees_get_personal_session_info_response_from_dict = TransportEmployeesGetPersonalSessionInfoResponse.from_dict(transport_employees_get_personal_session_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


