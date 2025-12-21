# IntervalDto3

Menu availability time intervals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization GUID | 
**from_time** | **str** | Start time | 
**to_time** | **str** | End time | 

## Example

```python
from iikocloud_client.models.interval_dto3 import IntervalDto3

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalDto3 from a JSON string
interval_dto3_instance = IntervalDto3.from_json(json)
# print the JSON string representation of the object
print(IntervalDto3.to_json())

# convert the object into a dict
interval_dto3_dict = interval_dto3_instance.to_dict()
# create an instance of IntervalDto3 from a dict
interval_dto3_from_dict = IntervalDto3.from_dict(interval_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


