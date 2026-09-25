# ExternalMenuV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_groups** | [**List[AllergenGroupDto]**](AllergenGroupDto.md) | Allergen groups | [optional] 
**button_image_url** | **str** | Link to image | [optional] 
**combo_categories** | [**List[ComboCategoryDto]**](ComboCategoryDto.md) |  | 
**customer_tag_groups** | [**List[CustomerTagGroup]**](CustomerTagGroup.md) | Customer tag groups | [optional] 
**description** | **str** | External menu description | [optional] [default to '']
**format_version** | **int** | Menu version | [default to 4]
**id** | **int** | ID of the external menu | 
**intervals** | [**List[IntervalDto]**](IntervalDto.md) | Menu availability time intervals | [optional] 
**item_groups** | [**List[ExternalMenuCategory3]**](ExternalMenuCategory3.md) |  | 
**name** | **str** | External menu name | [optional] [default to '']
**override_tax_categories** | **Dict[str, List[OverrideTaxesDto]]** | Tax benefits | [optional] 
**product_categories** | [**List[ProductCategoryDto]**](ProductCategoryDto.md) | Product categories | [optional] 
**revision** | **int** | Menu revision | [optional] 
**tax_categories** | [**List[TaxCategoryDto]**](TaxCategoryDto.md) | Tax Categories | [optional] 

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


