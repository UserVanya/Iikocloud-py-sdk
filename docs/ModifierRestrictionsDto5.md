# ModifierRestrictionsDto5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_quantity** | **int** | Minimum amount | [optional] [default to 0]
**max_quantity** | **int** | Maximum  amount | [optional] [default to 1]
**free_quantity** | **int** | Amount free of charge | [optional] [default to 0]
**by_default** | [**int**](Int.md) | Default amount | [optional] 
**hide_if_default_quantity** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.modifier_restrictions_dto5 import ModifierRestrictionsDto5

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierRestrictionsDto5 from a JSON string
modifier_restrictions_dto5_instance = ModifierRestrictionsDto5.from_json(json)
# print the JSON string representation of the object
print(ModifierRestrictionsDto5.to_json())

# convert the object into a dict
modifier_restrictions_dto5_dict = modifier_restrictions_dto5_instance.to_dict()
# create an instance of ModifierRestrictionsDto5 from a dict
modifier_restrictions_dto5_from_dict = ModifierRestrictionsDto5.from_dict(modifier_restrictions_dto5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


