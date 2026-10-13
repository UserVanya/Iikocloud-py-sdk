# MenuV3OverrideTaxCategory

Tax category override.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_tax_category_id** | **UUID** | Base tax category ID. | [optional] 
**new_tax_category_id** | **UUID** | New tax category ID to use instead of the base one. | [optional] 
**order_type_id** | **UUID** | Order type ID. If null, the override is applied to all order types. | [optional] 

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


