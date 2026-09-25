# EventMetadataListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_groups** | [**List[EventGroup]**](EventGroup.md) | Event groups | [optional] 
**total_count** | **int** | Total number of event groups | [optional] 

## Example

```python
from iikocloud_client.models.event_metadata_list_response import EventMetadataListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventMetadataListResponse from a JSON string
event_metadata_list_response_instance = EventMetadataListResponse.from_json(json)
# print the JSON string representation of the object
print(EventMetadataListResponse.to_json())

# convert the object into a dict
event_metadata_list_response_dict = event_metadata_list_response_instance.to_dict()
# create an instance of EventMetadataListResponse from a dict
event_metadata_list_response_from_dict = EventMetadataListResponse.from_dict(event_metadata_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


