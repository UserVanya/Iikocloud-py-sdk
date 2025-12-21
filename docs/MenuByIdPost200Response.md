# MenuByIdPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_categories** | [**List[ProductCategoryDto3]**](ProductCategoryDto3.md) | Product categories | [optional] 
**customer_tag_groups** | [**List[CustomerTagGroup3]**](CustomerTagGroup3.md) | Customer tag groups | [optional] 
**revision** | **int** | Menu revision | [optional] 
**format_version** | **int** | Menu version | [optional] [default to 2]
**id** | **int** | ID of the external menu | 
**name** | **str** | External menu name | [optional] [default to '']
**description** | **str** | External menu description | [optional] [default to '']
**button_image_url** | **str** | Link to image | [optional] 
**intervals** | [**List[IntervalDto3]**](IntervalDto3.md) | Menu availability time intervals | [optional] 
**item_categories** | [**List[ExternalMenuCategory]**](ExternalMenuCategory.md) |  | 
**combo_categories** | [**List[ComboCategoryDto3]**](ComboCategoryDto3.md) |  | 
**tax_categories** | [**List[TaxCategoryDto2]**](TaxCategoryDto2.md) | Tax Categories | [optional] 
**allergen_groups** | [**List[AllergenGroupDto2]**](AllergenGroupDto2.md) | Allergen groups | [optional] 
**override_tax_categories** | [**List[OverrideTaxesDto2]**](OverrideTaxesDto2.md) | Tax benefits | [optional] 
**item_groups** | [**List[ExternalMenuCategory3]**](ExternalMenuCategory3.md) |  | 

## Example

```python
from iikocloud_client.models.menu_by_id_post200_response import MenuByIdPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MenuByIdPost200Response from a JSON string
menu_by_id_post200_response_instance = MenuByIdPost200Response.from_json(json)
# print the JSON string representation of the object
print(MenuByIdPost200Response.to_json())

# convert the object into a dict
menu_by_id_post200_response_dict = menu_by_id_post200_response_instance.to_dict()
# create an instance of MenuByIdPost200Response from a dict
menu_by_id_post200_response_from_dict = MenuByIdPost200Response.from_dict(menu_by_id_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


