# AttendanceListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendance_type_ids** | **List[UUID]** | Non-empty unique array of attendance type UUIDs to filter by | [optional] 
**employee_ids** | **List[UUID]** | Non-empty unique array of employee UUIDs to filter by | [optional] 
**end_at** | **str** | Date and time of the confirmed attendance end. If the value is &#x60;null&#x60;, the attendance is considered open. Existing attendances may be open. | 
**is_closed** | **bool** | Attendance closed flag. If absent in the request body - both closed and open attendances will be returned. If the value is &#x60;true&#x60; - only closed attendances will be returned (&#x60;endAt !&#x3D; null&#x60;). If the value is &#x60;false&#x60; - only open attendances will be returned (&#x60;endAt &#x3D; null&#x60;) | [optional] 
**limit** | **int** | Maximum number of records in the response (1..1000) | [optional] 
**offset** | **int** | Number of records to skip from the beginning | [optional] 
**organization_id** | **UUID** | Organization UUID | 
**should_include_payment_details** | **bool** | Flag to display payment details | [optional] 
**start_at** | **str** | Date and time of the confirmed attendance start | 

## Example

```python
from iikocloud_client.models.attendance_list_request import AttendanceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceListRequest from a JSON string
attendance_list_request_instance = AttendanceListRequest.from_json(json)
# print the JSON string representation of the object
print(AttendanceListRequest.to_json())

# convert the object into a dict
attendance_list_request_dict = attendance_list_request_instance.to_dict()
# create an instance of AttendanceListRequest from a dict
attendance_list_request_from_dict = AttendanceListRequest.from_dict(attendance_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


