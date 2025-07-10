# ModifierRestrictionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_quantity** | **int** | Minimum amount | [optional] 
**max_quantity** | **int** | Maximum amount | [optional] 
**free_quantity** | **int** | Amount free of charge | [optional] 
**by_default** | **int** | Default amount | [optional] 

## Example

```python
from iiko_cloud_client.models.modifier_restrictions_dto import ModifierRestrictionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierRestrictionsDto from a JSON string
modifier_restrictions_dto_instance = ModifierRestrictionsDto.from_json(json)
# print the JSON string representation of the object
print(ModifierRestrictionsDto.to_json())

# convert the object into a dict
modifier_restrictions_dto_dict = modifier_restrictions_dto_instance.to_dict()
# create an instance of ModifierRestrictionsDto from a dict
modifier_restrictions_dto_from_dict = ModifierRestrictionsDto.from_dict(modifier_restrictions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


