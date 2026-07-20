# LabelDto2

Labels can be added to items to reflect a category (e.g. Vegan, Alcohol, Spicy, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Label code | [optional] [default to '']
**name** | **str** | Label name | [optional] [default to '']

## Example

```python
from iikocloud_client.models.label_dto2 import LabelDto2

# TODO update the JSON string below
json = "{}"
# create an instance of LabelDto2 from a JSON string
label_dto2_instance = LabelDto2.from_json(json)
# print the JSON string representation of the object
print(LabelDto2.to_json())

# convert the object into a dict
label_dto2_dict = label_dto2_instance.to_dict()
# create an instance of LabelDto2 from a dict
label_dto2_from_dict = LabelDto2.from_dict(label_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


