# CourierLocationsByTimeOffsetRequest

Request for coordinates history of drivers in OrganizationIds organizations.  If driver coordinates were recorded in server storage within interval:   [\"current server time\" - OffsetInSeconds, \"current server time\"),  driver and their coordinates will be retrieved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_in_seconds** | **int** | Interval in seconds from current server time.   If driver coordinates were recorded in server storage   within interval: (\&quot;current server time\&quot; - *OffsetInSeconds*, \&quot;current server time\&quot;],  driver and their coordinates will be retrieved. | [optional] 
**organization_ids** | **List[UUID]** | List of organizations for drivers coordinates of which will be retrieved. | 

## Example

```python
from iikocloud_client.models.courier_locations_by_time_offset_request import CourierLocationsByTimeOffsetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourierLocationsByTimeOffsetRequest from a JSON string
courier_locations_by_time_offset_request_instance = CourierLocationsByTimeOffsetRequest.from_json(json)
# print the JSON string representation of the object
print(CourierLocationsByTimeOffsetRequest.to_json())

# convert the object into a dict
courier_locations_by_time_offset_request_dict = courier_locations_by_time_offset_request_instance.to_dict()
# create an instance of CourierLocationsByTimeOffsetRequest from a dict
courier_locations_by_time_offset_request_from_dict = CourierLocationsByTimeOffsetRequest.from_dict(courier_locations_by_time_offset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


