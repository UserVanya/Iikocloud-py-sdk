# LabelDto

Labels can be added to items to reflect a category (e.g. Vegan, Alcohol, Spicy, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Label code | [optional] [default to '']
**name** | **str** | Label name | [optional] [default to '']

## Example

```python
from iikocloud_client.models.label_dto import LabelDto

# TODO update the JSON string below
json = "{}"
# create an instance of LabelDto from a JSON string
label_dto_instance = LabelDto.from_json(json)
# print the JSON string representation of the object
print(LabelDto.to_json())

# convert the object into a dict
label_dto_dict = label_dto_instance.to_dict()
# create an instance of LabelDto from a dict
label_dto_from_dict = LabelDto.from_dict(label_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


