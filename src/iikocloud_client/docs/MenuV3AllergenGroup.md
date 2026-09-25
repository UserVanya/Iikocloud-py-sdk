# MenuV3AllergenGroup

Allergen group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Allergen group code. | 
**id** | **str** | Allergen group ID. | 
**is_deleted** | **bool** | Flag indicating whether the group is deleted. | [optional] 
**name** | **str** | Allergen group name. | 

## Example

```python
from iikocloud_client.models.menu_v3_allergen_group import MenuV3AllergenGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3AllergenGroup from a JSON string
menu_v3_allergen_group_instance = MenuV3AllergenGroup.from_json(json)
# print the JSON string representation of the object
print(MenuV3AllergenGroup.to_json())

# convert the object into a dict
menu_v3_allergen_group_dict = menu_v3_allergen_group_instance.to_dict()
# create an instance of MenuV3AllergenGroup from a dict
menu_v3_allergen_group_from_dict = MenuV3AllergenGroup.from_dict(menu_v3_allergen_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


