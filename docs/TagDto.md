# TagDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.tag_dto import TagDto

# TODO update the JSON string below
json = "{}"
# create an instance of TagDto from a JSON string
tag_dto_instance = TagDto.from_json(json)
# print the JSON string representation of the object
print(TagDto.to_json())

# convert the object into a dict
tag_dto_dict = tag_dto_instance.to_dict()
# create an instance of TagDto from a dict
tag_dto_from_dict = TagDto.from_dict(tag_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


