# ExternalMenuV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_categories** | [**List[ProductCategoryDto]**](ProductCategoryDto.md) | Product categories | [optional] 
**customer_tag_groups** | [**List[CustomerTagGroup]**](CustomerTagGroup.md) | Customer tag groups | [optional] 
**revision** | **int** | Menu revision | [optional] 
**format_version** | **int** | Menu version | [optional] [default to 2]
**id** | **int** | ID of the external menu | 
**name** | **str** | External menu name | [optional] [default to '']
**description** | **str** | External menu description | [optional] [default to '']
**button_image_url** | **str** | Link to image | [optional] 
**intervals** | [**List[IntervalDto]**](IntervalDto.md) | Menu availability time intervals | [optional] 
**item_categories** | [**List[ExternalMenuCategory]**](ExternalMenuCategory.md) |  | 
**combo_categories** | [**List[ComboCategoryDto]**](ComboCategoryDto.md) |  | 

## Example

```python
from iikocloud_client.models.external_menu_v2 import ExternalMenuV2

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuV2 from a JSON string
external_menu_v2_instance = ExternalMenuV2.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuV2.to_json())

# convert the object into a dict
external_menu_v2_dict = external_menu_v2_instance.to_dict()
# create an instance of ExternalMenuV2 from a dict
external_menu_v2_from_dict = ExternalMenuV2.from_dict(external_menu_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


