# ModifierRestrictionsDto7


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_quantity** | **int** | Minimum amount | [optional] [default to 0]
**max_quantity** | **int** | Maximum  amount | [optional] [default to 1]
**free_quantity** | **int** | Amount free of charge | [optional] [default to 0]
**hide_if_default_quantity** | **bool** |  | [optional] [default to False]
**default_quantity** | [**int**](Int.md) | Default amount | 

## Example

```python
from iikocloud_client.models.modifier_restrictions_dto7 import ModifierRestrictionsDto7

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierRestrictionsDto7 from a JSON string
modifier_restrictions_dto7_instance = ModifierRestrictionsDto7.from_json(json)
# print the JSON string representation of the object
print(ModifierRestrictionsDto7.to_json())

# convert the object into a dict
modifier_restrictions_dto7_dict = modifier_restrictions_dto7_instance.to_dict()
# create an instance of ModifierRestrictionsDto7 from a dict
modifier_restrictions_dto7_from_dict = ModifierRestrictionsDto7.from_dict(modifier_restrictions_dto7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


