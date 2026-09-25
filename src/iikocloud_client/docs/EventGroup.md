# EventGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Event group code | [optional] 
**event_types** | [**List[EventType]**](EventType.md) | Event types of the group | [optional] 
**name** | **str** | Event group name | [optional] 

## Example

```python
from iikocloud_client.models.event_group import EventGroup

# TODO update the JSON string below
json = "{}"
# create an instance of EventGroup from a JSON string
event_group_instance = EventGroup.from_json(json)
# print the JSON string representation of the object
print(EventGroup.to_json())

# convert the object into a dict
event_group_dict = event_group_instance.to_dict()
# create an instance of EventGroup from a dict
event_group_from_dict = EventGroup.from_dict(event_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


