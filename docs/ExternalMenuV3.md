# ExternalMenuV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_categories** | [**List[TaxCategoryDto]**](TaxCategoryDto.md) | Tax Categories | [optional] 
**product_categories** | [**List[ProductCategoryDto2]**](ProductCategoryDto2.md) | Product categories | [optional] 
**allergen_groups** | [**List[AllergenGroupDto]**](AllergenGroupDto.md) | Allergen groups | [optional] 
**customer_tag_groups** | [**List[CustomerTagGroup2]**](CustomerTagGroup2.md) | Customer tag groups | [optional] 
**override_tax_categories** | **Dict[str, List[OverrideTaxesDto]]** | Tax benefits | [optional] 
**revision** | **int** | Menu revision | [optional] 
**format_version** | **int** | Menu version | [optional] [default to 2]
**id** | **int** | ID of the external menu | 
**name** | **str** | External menu name | [optional] [default to '']
**description** | **str** | External menu description | [optional] [default to '']
**button_image_url** | **str** | Link to image | [optional] 
**intervals** | [**List[IntervalDto2]**](IntervalDto2.md) | Menu availability time intervals | [optional] 
**combo_categories** | [**List[ComboCategoryDto2]**](ComboCategoryDto2.md) |  | 
**item_groups** | [**List[ExternalMenuCategory2]**](ExternalMenuCategory2.md) |  | 

## Example

```python
from iikocloud_client.models.external_menu_v3 import ExternalMenuV3

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuV3 from a JSON string
external_menu_v3_instance = ExternalMenuV3.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuV3.to_json())

# convert the object into a dict
external_menu_v3_dict = external_menu_v3_instance.to_dict()
# create an instance of ExternalMenuV3 from a dict
external_menu_v3_from_dict = ExternalMenuV3.from_dict(external_menu_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


