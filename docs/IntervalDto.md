# IntervalDto

Menu availability time intervals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization GUID | 
**from_time** | **str** | Start time | 
**to_time** | **str** | End time | 

## Example

```python
from iikocloud_client.models.interval_dto import IntervalDto

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalDto from a JSON string
interval_dto_instance = IntervalDto.from_json(json)
# print the JSON string representation of the object
print(IntervalDto.to_json())

# convert the object into a dict
interval_dto_dict = interval_dto_instance.to_dict()
# create an instance of IntervalDto from a dict
interval_dto_from_dict = IntervalDto.from_dict(interval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


