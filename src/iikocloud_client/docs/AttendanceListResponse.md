# AttendanceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AttendanceResponse]**](AttendanceResponse.md) | Attendances | [optional] 
**limit** | **int** | Maximum number of records in the response (1..1000) | [optional] 
**offset** | **int** | Number of records to skip from the beginning | [optional] 
**total_count** | **int** | Total number of records matching the selected filter rules | [optional] 

## Example

```python
from iikocloud_client.models.attendance_list_response import AttendanceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceListResponse from a JSON string
attendance_list_response_instance = AttendanceListResponse.from_json(json)
# print the JSON string representation of the object
print(AttendanceListResponse.to_json())

# convert the object into a dict
attendance_list_response_dict = attendance_list_response_instance.to_dict()
# create an instance of AttendanceListResponse from a dict
attendance_list_response_from_dict = AttendanceListResponse.from_dict(attendance_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


