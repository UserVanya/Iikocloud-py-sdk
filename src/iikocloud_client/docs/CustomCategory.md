# CustomCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.custom_category import CustomCategory

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCategory from a JSON string
custom_category_instance = CustomCategory.from_json(json)
# print the JSON string representation of the object
print(CustomCategory.to_json())

# convert the object into a dict
custom_category_dict = custom_category_instance.to_dict()
# create an instance of CustomCategory from a dict
custom_category_from_dict = CustomCategory.from_dict(custom_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


