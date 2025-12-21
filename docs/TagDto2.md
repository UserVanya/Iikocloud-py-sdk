# TagDto2

List of tags

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tag GUID | [optional] [default to '']
**name** | **str** | Tag name | [optional] [default to '']

## Example

```python
from iikocloud_client.models.tag_dto2 import TagDto2

# TODO update the JSON string below
json = "{}"
# create an instance of TagDto2 from a JSON string
tag_dto2_instance = TagDto2.from_json(json)
# print the JSON string representation of the object
print(TagDto2.to_json())

# convert the object into a dict
tag_dto2_dict = tag_dto2_instance.to_dict()
# create an instance of TagDto2 from a dict
tag_dto2_from_dict = TagDto2.from_dict(tag_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


