# AttendanceTypeListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** | false — active, true — deleted, null — all | [optional] 
**limit** | **int** | Maximum number of records in the response (1..1000) | [optional] 
**offset** | **int** | Number of records to skip from the beginning | [optional] 

## Example

```python
from iikocloud_client.models.attendance_type_list_request import AttendanceTypeListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceTypeListRequest from a JSON string
attendance_type_list_request_instance = AttendanceTypeListRequest.from_json(json)
# print the JSON string representation of the object
print(AttendanceTypeListRequest.to_json())

# convert the object into a dict
attendance_type_list_request_dict = attendance_type_list_request_instance.to_dict()
# create an instance of AttendanceTypeListRequest from a dict
attendance_type_list_request_from_dict = AttendanceTypeListRequest.from_dict(attendance_type_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


