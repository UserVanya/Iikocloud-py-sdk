# EmployeesCourierLocationsByTimeOffsetResponse

DTO containing driver coordinates details for the last N seconds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**courier_locations** | [**List[WrapperEmployeesCourierLocations]**](WrapperEmployeesCourierLocations.md) | List of drivers&#39; coordinates broken down by organizations. | 

## Example

```python
from iikocloud_client.models.employees_courier_locations_by_time_offset_response import EmployeesCourierLocationsByTimeOffsetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesCourierLocationsByTimeOffsetResponse from a JSON string
employees_courier_locations_by_time_offset_response_instance = EmployeesCourierLocationsByTimeOffsetResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesCourierLocationsByTimeOffsetResponse.to_json())

# convert the object into a dict
employees_courier_locations_by_time_offset_response_dict = employees_courier_locations_by_time_offset_response_instance.to_dict()
# create an instance of EmployeesCourierLocationsByTimeOffsetResponse from a dict
employees_courier_locations_by_time_offset_response_from_dict = EmployeesCourierLocationsByTimeOffsetResponse.from_dict(employees_courier_locations_by_time_offset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


