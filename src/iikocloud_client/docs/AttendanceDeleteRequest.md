# AttendanceDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Attendance UUID | 
**organization_id** | **UUID** | Organization UUID | 

## Example

```python
from iikocloud_client.models.attendance_delete_request import AttendanceDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceDeleteRequest from a JSON string
attendance_delete_request_instance = AttendanceDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(AttendanceDeleteRequest.to_json())

# convert the object into a dict
attendance_delete_request_dict = attendance_delete_request_instance.to_dict()
# create an instance of AttendanceDeleteRequest from a dict
attendance_delete_request_from_dict = AttendanceDeleteRequest.from_dict(attendance_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


