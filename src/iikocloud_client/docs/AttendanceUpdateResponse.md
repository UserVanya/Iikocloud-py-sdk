# AttendanceUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendance** | [**AttendanceResponse**](AttendanceResponse.md) | Attendance | [optional] 

## Example

```python
from iikocloud_client.models.attendance_update_response import AttendanceUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceUpdateResponse from a JSON string
attendance_update_response_instance = AttendanceUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(AttendanceUpdateResponse.to_json())

# convert the object into a dict
attendance_update_response_dict = attendance_update_response_instance.to_dict()
# create an instance of AttendanceUpdateResponse from a dict
attendance_update_response_from_dict = AttendanceUpdateResponse.from_dict(attendance_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


