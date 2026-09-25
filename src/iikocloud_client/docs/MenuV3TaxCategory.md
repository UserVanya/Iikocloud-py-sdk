# MenuV3TaxCategory

Tax category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tax category ID. | 
**is_deleted** | **bool** | Flag indicating whether the category is deleted. | [optional] 
**name** | **str** | Tax category name. | 
**percentage** | **float** | Tax percentage. | 

## Example

```python
from iikocloud_client.models.menu_v3_tax_category import MenuV3TaxCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3TaxCategory from a JSON string
menu_v3_tax_category_instance = MenuV3TaxCategory.from_json(json)
# print the JSON string representation of the object
print(MenuV3TaxCategory.to_json())

# convert the object into a dict
menu_v3_tax_category_dict = menu_v3_tax_category_instance.to_dict()
# create an instance of MenuV3TaxCategory from a dict
menu_v3_tax_category_from_dict = MenuV3TaxCategory.from_dict(menu_v3_tax_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


