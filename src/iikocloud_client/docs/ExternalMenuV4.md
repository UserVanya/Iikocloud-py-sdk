# ExternalMenuV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_groups** | [**List[AllergenGroupDto2]**](AllergenGroupDto2.md) | Allergen groups | [optional] 
**button_image_url** | **str** | Link to image | [optional] 
**combo_categories** | [**List[ComboCategoryDto3]**](ComboCategoryDto3.md) |  | 
**customer_tag_groups** | [**List[CustomerTagGroup3]**](CustomerTagGroup3.md) | Customer tag groups | [optional] 
**description** | **str** | External menu description | [optional] [default to '']
**format_version** | **int** | Menu version | [default to 4]
**id** | **int** | ID of the external menu | 
**intervals** | [**List[IntervalDto3]**](IntervalDto3.md) | Menu availability time intervals | [optional] 
**item_groups** | [**List[ExternalMenuCategory3]**](ExternalMenuCategory3.md) |  | 
**name** | **str** | External menu name | [optional] [default to '']
**override_tax_categories** | **Dict[str, List[OverrideTaxesDto2]]** | Tax benefits | [optional] 
**product_categories** | [**List[ProductCategoryDto3]**](ProductCategoryDto3.md) | Product categories | [optional] 
**revision** | **int** | Menu revision | [optional] 
**tax_categories** | [**List[TaxCategoryDto2]**](TaxCategoryDto2.md) | Tax Categories | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_v4 import ExternalMenuV4

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuV4 from a JSON string
external_menu_v4_instance = ExternalMenuV4.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuV4.to_json())

# convert the object into a dict
external_menu_v4_dict = external_menu_v4_instance.to_dict()
# create an instance of ExternalMenuV4 from a dict
external_menu_v4_from_dict = ExternalMenuV4.from_dict(external_menu_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


