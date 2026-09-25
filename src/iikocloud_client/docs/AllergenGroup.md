# AllergenGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the directory entry | [optional] 
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.allergen_group import AllergenGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AllergenGroup from a JSON string
allergen_group_instance = AllergenGroup.from_json(json)
# print the JSON string representation of the object
print(AllergenGroup.to_json())

# convert the object into a dict
allergen_group_dict = allergen_group_instance.to_dict()
# create an instance of AllergenGroup from a dict
allergen_group_from_dict = AllergenGroup.from_dict(allergen_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


