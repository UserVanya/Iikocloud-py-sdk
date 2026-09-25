# AttendanceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendance_type_id** | **UUID** | Attendance type UUID | [optional] 
**comment** | **str** | Comment | [optional] 
**employee_id** | **UUID** | Employee UUID | 
**end_at** | **str** | Date and time of the confirmed attendance end. If the value is &#x60;null&#x60;, the attendance is considered open. Existing attendances may be open. | 
**is_confirmed_manually** | **bool** | Manually confirmed flag; may be absent for legacy data. | [optional] 
**organization_id** | **UUID** | Organization UUID | 
**personal_end_at** | **str** | Date and time of the registered attendance end from POS | [optional] 
**personal_start_at** | **str** | Date and time of the registered attendance start from POS | [optional] 
**role_id** | **UUID** | Role UUID; may be absent for legacy attendances | 
**start_at** | **str** | Date and time of the confirmed attendance start | 

## Example

```python
from iikocloud_client.models.attendance_create_request import AttendanceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceCreateRequest from a JSON string
attendance_create_request_instance = AttendanceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AttendanceCreateRequest.to_json())

# convert the object into a dict
attendance_create_request_dict = attendance_create_request_instance.to_dict()
# create an instance of AttendanceCreateRequest from a dict
attendance_create_request_from_dict = AttendanceCreateRequest.from_dict(attendance_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


