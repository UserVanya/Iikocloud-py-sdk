# AllergenGroupDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [default to '']
**code** | **str** | Allergen&#39;s code | [optional] [default to '']
**name** | **str** | Allergen&#39;s name | [optional] [default to '']
**is_deleted** | [**bool**](Bool.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.allergen_group_dto3 import AllergenGroupDto3

# TODO update the JSON string below
json = "{}"
# create an instance of AllergenGroupDto3 from a JSON string
allergen_group_dto3_instance = AllergenGroupDto3.from_json(json)
# print the JSON string representation of the object
print(AllergenGroupDto3.to_json())

# convert the object into a dict
allergen_group_dto3_dict = allergen_group_dto3_instance.to_dict()
# create an instance of AllergenGroupDto3 from a dict
allergen_group_dto3_from_dict = AllergenGroupDto3.from_dict(allergen_group_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


