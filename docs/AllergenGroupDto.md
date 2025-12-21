# AllergenGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [default to '']
**code** | **str** | Allergen&#39;s code | [optional] [default to '']
**name** | **str** | Allergen&#39;s name | [optional] [default to '']
**is_deleted** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.allergen_group_dto import AllergenGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of AllergenGroupDto from a JSON string
allergen_group_dto_instance = AllergenGroupDto.from_json(json)
# print the JSON string representation of the object
print(AllergenGroupDto.to_json())

# convert the object into a dict
allergen_group_dto_dict = allergen_group_dto_instance.to_dict()
# create an instance of AllergenGroupDto from a dict
allergen_group_dto_from_dict = AllergenGroupDto.from_dict(allergen_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


