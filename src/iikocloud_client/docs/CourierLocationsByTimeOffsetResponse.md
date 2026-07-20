# CourierLocationsByTimeOffsetResponse

DTO containing driver coordinates details for the last N seconds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**courier_locations** | [**List[RmsCourierLocationsItemsResponse]**](RmsCourierLocationsItemsResponse.md) | List of drivers&#39; coordinates broken down by organizations. | 

## Example

```python
from iikocloud_client.models.courier_locations_by_time_offset_response import CourierLocationsByTimeOffsetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourierLocationsByTimeOffsetResponse from a JSON string
courier_locations_by_time_offset_response_instance = CourierLocationsByTimeOffsetResponse.from_json(json)
# print the JSON string representation of the object
print(CourierLocationsByTimeOffsetResponse.to_json())

# convert the object into a dict
courier_locations_by_time_offset_response_dict = courier_locations_by_time_offset_response_instance.to_dict()
# create an instance of CourierLocationsByTimeOffsetResponse from a dict
courier_locations_by_time_offset_response_from_dict = CourierLocationsByTimeOffsetResponse.from_dict(courier_locations_by_time_offset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


