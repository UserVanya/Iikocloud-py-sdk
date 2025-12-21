# ModifierRestrictionsDto2


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
from iikocloud_client.models.modifier_restrictions_dto2 import ModifierRestrictionsDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierRestrictionsDto2 from a JSON string
modifier_restrictions_dto2_instance = ModifierRestrictionsDto2.from_json(json)
# print the JSON string representation of the object
print(ModifierRestrictionsDto2.to_json())

# convert the object into a dict
modifier_restrictions_dto2_dict = modifier_restrictions_dto2_instance.to_dict()
# create an instance of ModifierRestrictionsDto2 from a dict
modifier_restrictions_dto2_from_dict = ModifierRestrictionsDto2.from_dict(modifier_restrictions_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


