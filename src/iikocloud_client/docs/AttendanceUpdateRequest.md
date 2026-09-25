# AttendanceUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendance_type_id** | **UUID** | Attendance type UUID | 
**comment** | **str** | Comment | [optional] 
**employee_id** | **UUID** | Employee UUID | 
**end_at** | **str** | Date and time of the confirmed attendance end. If the value is &#x60;null&#x60;, the attendance is considered open. Existing attendances may be open. | 
**id** | **UUID** | Attendance UUID | 
**is_confirmed_manually** | **bool** | Manually confirmed flag; may be absent for legacy data | 
**organization_id** | **UUID** | Organization UUID | 
**personal_end_at** | **str** | Date and time of the registered attendance end from POS. An already set value cannot be reset (set to &#x60;null&#x60;). | [optional] 
**personal_start_at** | **str** | Date and time of the registered attendance start from POS. An already set value cannot be reset (set to &#x60;null&#x60;). | [optional] 
**role_id** | **UUID** | Role UUID; may be absent for legacy attendances | 
**start_at** | **str** | Date and time of the confirmed attendance start | 

## Example

```python
from iikocloud_client.models.attendance_update_request import AttendanceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceUpdateRequest from a JSON string
attendance_update_request_instance = AttendanceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AttendanceUpdateRequest.to_json())

# convert the object into a dict
attendance_update_request_dict = attendance_update_request_instance.to_dict()
# create an instance of AttendanceUpdateRequest from a dict
attendance_update_request_from_dict = AttendanceUpdateRequest.from_dict(attendance_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


