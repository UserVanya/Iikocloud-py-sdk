# TransportEmployeesCourierLocationsByTimeOffsetRequest

Request for coordinates history of drivers in OrganizationIds organizations.  If driver coordinates were recorded in server storage within interval:   [\"current server time\" - OffsetInSeconds, \"current server time\"),  driver and their coordinates will be retrieved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | List of organizations for drivers coordinates of which will be retrieved. | 
**offset_in_seconds** | **int** | Interval in seconds from current server time.   If driver coordinates were recorded in server storage   within interval: (\&quot;current server time\&quot; - *OffsetInSeconds*, \&quot;current server time\&quot;],  driver and their coordinates will be retrieved. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_employees_courier_locations_by_time_offset_request import TransportEmployeesCourierLocationsByTimeOffsetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesCourierLocationsByTimeOffsetRequest from a JSON string
transport_employees_courier_locations_by_time_offset_request_instance = TransportEmployeesCourierLocationsByTimeOffsetRequest.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesCourierLocationsByTimeOffsetRequest.to_json())

# convert the object into a dict
transport_employees_courier_locations_by_time_offset_request_dict = transport_employees_courier_locations_by_time_offset_request_instance.to_dict()
# create an instance of TransportEmployeesCourierLocationsByTimeOffsetRequest from a dict
transport_employees_courier_locations_by_time_offset_request_from_dict = TransportEmployeesCourierLocationsByTimeOffsetRequest.from_dict(transport_employees_courier_locations_by_time_offset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


