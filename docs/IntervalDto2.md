# IntervalDto2

Menu availability time intervals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization GUID | 
**from_time** | **str** | Start time | 
**to_time** | **str** | End time | 

## Example

```python
from iikocloud_client.models.interval_dto2 import IntervalDto2

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalDto2 from a JSON string
interval_dto2_instance = IntervalDto2.from_json(json)
# print the JSON string representation of the object
print(IntervalDto2.to_json())

# convert the object into a dict
interval_dto2_dict = interval_dto2_instance.to_dict()
# create an instance of IntervalDto2 from a dict
interval_dto2_from_dict = IntervalDto2.from_dict(interval_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


