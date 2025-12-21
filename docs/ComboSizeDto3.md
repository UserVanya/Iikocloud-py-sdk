# ComboSizeDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**button_image** | [**ButtonImageDto3**](ButtonImageDto3.md) |  | [optional] 
**short_name** | **str** |  | 

## Example

```python
from iikocloud_client.models.combo_size_dto3 import ComboSizeDto3

# TODO update the JSON string below
json = "{}"
# create an instance of ComboSizeDto3 from a JSON string
combo_size_dto3_instance = ComboSizeDto3.from_json(json)
# print the JSON string representation of the object
print(ComboSizeDto3.to_json())

# convert the object into a dict
combo_size_dto3_dict = combo_size_dto3_instance.to_dict()
# create an instance of ComboSizeDto3 from a dict
combo_size_dto3_from_dict = ComboSizeDto3.from_dict(combo_size_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


