# AttendanceDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Attendance UUID | [optional] 

## Example

```python
from iikocloud_client.models.attendance_delete_response import AttendanceDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceDeleteResponse from a JSON string
attendance_delete_response_instance = AttendanceDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(AttendanceDeleteResponse.to_json())

# convert the object into a dict
attendance_delete_response_dict = attendance_delete_response_instance.to_dict()
# create an instance of AttendanceDeleteResponse from a dict
attendance_delete_response_from_dict = AttendanceDeleteResponse.from_dict(attendance_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


