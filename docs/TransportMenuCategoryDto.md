# TransportMenuCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TransportItemDto]**](TransportItemDto.md) |  | [optional] 
**id** | **str** | ID of the category of the external menu | [optional] 
**name** | **str** | Category name of the external menu | [optional] 
**description** | **str** | Category description | [optional] 
**button_image_url** | **str** | Links to images | [optional] 
**header_image_url** | **str** | Description header for the images | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_menu_category_dto import TransportMenuCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransportMenuCategoryDto from a JSON string
transport_menu_category_dto_instance = TransportMenuCategoryDto.from_json(json)
# print the JSON string representation of the object
print(TransportMenuCategoryDto.to_json())

# convert the object into a dict
transport_menu_category_dto_dict = transport_menu_category_dto_instance.to_dict()
# create an instance of TransportMenuCategoryDto from a dict
transport_menu_category_dto_from_dict = TransportMenuCategoryDto.from_dict(transport_menu_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


