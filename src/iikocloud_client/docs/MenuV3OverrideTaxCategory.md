# MenuV3OverrideTaxCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_tax_category_id** | **str** | Base tax category ID. | [optional] 
**new_tax_category_id** | **str** | Tax category ID applied instead. | [optional] 
**order_type_id** | **str** | Order type ID. | [optional] 

## Example

```python
from iikocloud_client.models.menu_v3_override_tax_category import MenuV3OverrideTaxCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3OverrideTaxCategory from a JSON string
menu_v3_override_tax_category_instance = MenuV3OverrideTaxCategory.from_json(json)
# print the JSON string representation of the object
print(MenuV3OverrideTaxCategory.to_json())

# convert the object into a dict
menu_v3_override_tax_category_dict = menu_v3_override_tax_category_instance.to_dict()
# create an instance of MenuV3OverrideTaxCategory from a dict
menu_v3_override_tax_category_from_dict = MenuV3OverrideTaxCategory.from_dict(menu_v3_override_tax_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


