# EventListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[EventAttributeDoc]**](EventAttributeDoc.md) | Event attributes | [optional] 
**event_type** | **str** | Event type code | [optional] 
**id** | **UUID** | Event identifier (UUID), unique | [optional] 
**occurred_at** | **str** | Event date and time | [optional] 
**source** | **str** | Data source: &#x60;RMS&#x60; if organizationId is provided in the request, otherwise &#x60;Chain&#x60; | [optional] 

## Example

```python
from iikocloud_client.models.event_list_item import EventListItem

# TODO update the JSON string below
json = "{}"
# create an instance of EventListItem from a JSON string
event_list_item_instance = EventListItem.from_json(json)
# print the JSON string representation of the object
print(EventListItem.to_json())

# convert the object into a dict
event_list_item_dict = event_list_item_instance.to_dict()
# create an instance of EventListItem from a dict
event_list_item_from_dict = EventListItem.from_dict(event_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


