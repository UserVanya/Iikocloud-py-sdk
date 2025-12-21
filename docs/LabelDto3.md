# LabelDto3

Labels can be added to items to reflect a category (e.g. Vegan, Alcohol, Spicy, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Label code | [optional] [default to '']
**name** | **str** | Label name | [optional] [default to '']

## Example

```python
from iikocloud_client.models.label_dto3 import LabelDto3

# TODO update the JSON string below
json = "{}"
# create an instance of LabelDto3 from a JSON string
label_dto3_instance = LabelDto3.from_json(json)
# print the JSON string representation of the object
print(LabelDto3.to_json())

# convert the object into a dict
label_dto3_dict = label_dto3_instance.to_dict()
# create an instance of LabelDto3 from a dict
label_dto3_from_dict = LabelDto3.from_dict(label_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


