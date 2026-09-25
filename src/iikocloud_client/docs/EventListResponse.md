# EventListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EventListItem]**](EventListItem.md) |  | [optional] 
**revision** | **int** | Revision up to which events are returned inclusively. Use revision + 1 for the next request | [optional] 
**total_count** | **int** | Total number of events in the response | [optional] 

## Example

```python
from iikocloud_client.models.event_list_response import EventListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventListResponse from a JSON string
event_list_response_instance = EventListResponse.from_json(json)
# print the JSON string representation of the object
print(EventListResponse.to_json())

# convert the object into a dict
event_list_response_dict = event_list_response_instance.to_dict()
# create an instance of EventListResponse from a dict
event_list_response_from_dict = EventListResponse.from_dict(event_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


