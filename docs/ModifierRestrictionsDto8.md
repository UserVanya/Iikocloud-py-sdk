# ModifierRestrictionsDto8


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_quantity** | **int** | Minimum amount | [optional] [default to 0]
**max_quantity** | **int** | Maximum  amount | [optional] [default to 1]
**free_quantity** | **int** | Amount free of charge | [optional] [default to 0]
**hide_if_default_quantity** | **bool** |  | [optional] [default to False]
**default_quantity** | **int** | Default amount | 

## Example

```python
from iikocloud_client.models.modifier_restrictions_dto8 import ModifierRestrictionsDto8

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierRestrictionsDto8 from a JSON string
modifier_restrictions_dto8_instance = ModifierRestrictionsDto8.from_json(json)
# print the JSON string representation of the object
print(ModifierRestrictionsDto8.to_json())

# convert the object into a dict
modifier_restrictions_dto8_dict = modifier_restrictions_dto8_instance.to_dict()
# create an instance of ModifierRestrictionsDto8 from a dict
modifier_restrictions_dto8_from_dict = ModifierRestrictionsDto8.from_dict(modifier_restrictions_dto8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


