# ComboSizeDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**button_image** | [**ButtonImageDto2**](ButtonImageDto2.md) |  | [optional] 
**short_name** | **str** |  | 

## Example

```python
from iikocloud_client.models.combo_size_dto2 import ComboSizeDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ComboSizeDto2 from a JSON string
combo_size_dto2_instance = ComboSizeDto2.from_json(json)
# print the JSON string representation of the object
print(ComboSizeDto2.to_json())

# convert the object into a dict
combo_size_dto2_dict = combo_size_dto2_instance.to_dict()
# create an instance of ComboSizeDto2 from a dict
combo_size_dto2_from_dict = ComboSizeDto2.from_dict(combo_size_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


