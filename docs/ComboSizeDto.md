# ComboSizeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**button_image** | [**ButtonImageDto**](ButtonImageDto.md) |  | [optional] 
**short_name** | **str** |  | 

## Example

```python
from iikocloud_client.models.combo_size_dto import ComboSizeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComboSizeDto from a JSON string
combo_size_dto_instance = ComboSizeDto.from_json(json)
# print the JSON string representation of the object
print(ComboSizeDto.to_json())

# convert the object into a dict
combo_size_dto_dict = combo_size_dto_instance.to_dict()
# create an instance of ComboSizeDto from a dict
combo_size_dto_from_dict = ComboSizeDto.from_dict(combo_size_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


