# ExternalMenuResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_image_url** | **str** | Link to image | [optional] 
**combo_categories** | [**List[ComboCategoryDto3]**](ComboCategoryDto3.md) |  | 
**customer_tag_groups** | [**List[CustomerTagGroup3]**](CustomerTagGroup3.md) | Customer tag groups | [optional] 
**description** | **str** | External menu description | [optional] [default to '']
**format_version** | **int** | Menu version | [default to 4]
**id** | **int** | ID of the external menu | 
**intervals** | [**List[IntervalDto3]**](IntervalDto3.md) | Menu availability time intervals | [optional] 
**item_categories** | [**List[ExternalMenuCategory]**](ExternalMenuCategory.md) |  | 
**name** | **str** | External menu name | [optional] [default to '']
**product_categories** | [**List[ProductCategoryDto3]**](ProductCategoryDto3.md) | Product categories | [optional] 
**revision** | **int** | Menu revision | [optional] 
**allergen_groups** | [**List[AllergenGroupDto2]**](AllergenGroupDto2.md) | Allergen groups | [optional] 
**item_groups** | [**List[ExternalMenuCategory3]**](ExternalMenuCategory3.md) |  | 
**override_tax_categories** | **Dict[str, List[OverrideTaxesDto2]]** | Tax benefits | [optional] 
**tax_categories** | [**List[TaxCategoryDto2]**](TaxCategoryDto2.md) | Tax Categories | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_response import ExternalMenuResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuResponse from a JSON string
external_menu_response_instance = ExternalMenuResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuResponse.to_json())

# convert the object into a dict
external_menu_response_dict = external_menu_response_instance.to_dict()
# create an instance of ExternalMenuResponse from a dict
external_menu_response_from_dict = ExternalMenuResponse.from_dict(external_menu_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


