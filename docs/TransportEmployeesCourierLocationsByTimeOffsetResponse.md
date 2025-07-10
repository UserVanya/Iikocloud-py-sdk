# TransportEmployeesCourierLocationsByTimeOffsetResponse

DTO containing driver coordinates details for the last N seconds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**courier_locations** | [**List[TransportCommonRmsItemsResponseWrapperCourierLocations]**](TransportCommonRmsItemsResponseWrapperCourierLocations.md) | List of drivers&#39; coordinates broken down by organizations. | 

## Example

```python
from iiko_cloud_client.models.transport_employees_courier_locations_by_time_offset_response import TransportEmployeesCourierLocationsByTimeOffsetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesCourierLocationsByTimeOffsetResponse from a JSON string
transport_employees_courier_locations_by_time_offset_response_instance = TransportEmployeesCourierLocationsByTimeOffsetResponse.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesCourierLocationsByTimeOffsetResponse.to_json())

# convert the object into a dict
transport_employees_courier_locations_by_time_offset_response_dict = transport_employees_courier_locations_by_time_offset_response_instance.to_dict()
# create an instance of TransportEmployeesCourierLocationsByTimeOffsetResponse from a dict
transport_employees_courier_locations_by_time_offset_response_from_dict = TransportEmployeesCourierLocationsByTimeOffsetResponse.from_dict(transport_employees_courier_locations_by_time_offset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


