# EventListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_types** | **List[str]** | Event codes to filter by. If omitted or empty, all events are returned | [optional] 
**from_revision** | **int** | Revision to request events from (incremental mode). Cannot be combined with fromTime/toTime | [optional] 
**from_time** | **str** | Period start, inclusive, date-time format. Must be provided together with toTime | [optional] 
**organization_id** | **UUID** | Organization identifier (GUID). If provided, the request goes to the RMS API; otherwise to the Chain API by userContext.uocId | [optional] 
**to_time** | **str** | Period end, exclusive, date-time format. Must be provided together with fromTime | [optional] 

## Example

```python
from iikocloud_client.models.event_list_request import EventListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventListRequest from a JSON string
event_list_request_instance = EventListRequest.from_json(json)
# print the JSON string representation of the object
print(EventListRequest.to_json())

# convert the object into a dict
event_list_request_dict = event_list_request_instance.to_dict()
# create an instance of EventListRequest from a dict
event_list_request_from_dict = EventListRequest.from_dict(event_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


