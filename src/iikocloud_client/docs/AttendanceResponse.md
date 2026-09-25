# AttendanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendance_type_code** | **str** | Attendance type code | [optional] 
**attendance_type_id** | **UUID** | Attendance type UUID | [optional] 
**comment** | **str** | Comment | [optional] 
**created_at** | **str** | Date and time of creation | [optional] 
**employee_id** | **UUID** | Employee UUID | [optional] 
**end_at** | **str** | Date and time of the confirmed attendance end. If the value is &#x60;null&#x60;, the attendance is considered open. Existing attendances may be open. | [optional] 
**id** | **UUID** | Attendance UUID | [optional] 
**is_closed** | **bool** | Attendance closed flag. Computed as endAt !&#x3D; null | [optional] 
**is_confirmed_manually** | **bool** | Manually confirmed flag; may be absent for legacy data | [optional] 
**modified_by_user_id** | **str** | UUID of the user who made the last changes | [optional] 
**organization_id** | **UUID** | Organization UUID | [optional] 
**organization_name** | **str** | Organization name | [optional] 
**payment_details** | [**PaymentDetails**](PaymentDetails.md) | Payment calculation; null if not requested or not applicable | [optional] 
**personal_end_at** | **str** | Date and time of the registered attendance end from POS | [optional] 
**personal_start_at** | **str** | Date and time of the registered attendance start from POS | [optional] 
**role_id** | **UUID** | Role UUID; may be absent for legacy attendances | [optional] 
**start_at** | **str** | Date and time of the confirmed attendance start | [optional] 
**updated_at** | **str** | Date and time of the last modification | [optional] 

## Example

```python
from iikocloud_client.models.attendance_response import AttendanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceResponse from a JSON string
attendance_response_instance = AttendanceResponse.from_json(json)
# print the JSON string representation of the object
print(AttendanceResponse.to_json())

# convert the object into a dict
attendance_response_dict = attendance_response_instance.to_dict()
# create an instance of AttendanceResponse from a dict
attendance_response_from_dict = AttendanceResponse.from_dict(attendance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


