# AttendanceCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendance** | [**AttendanceResponse**](AttendanceResponse.md) | Attendance | [optional] 

## Example

```python
from iikocloud_client.models.attendance_create_response import AttendanceCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceCreateResponse from a JSON string
attendance_create_response_instance = AttendanceCreateResponse.from_json(json)
# print the JSON string representation of the object
print(AttendanceCreateResponse.to_json())

# convert the object into a dict
attendance_create_response_dict = attendance_create_response_instance.to_dict()
# create an instance of AttendanceCreateResponse from a dict
attendance_create_response_from_dict = AttendanceCreateResponse.from_dict(attendance_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


