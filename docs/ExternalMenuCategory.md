# ExternalMenuCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category ID | [optional] 
**name** | **str** | Category name | [optional] [default to '']
**description** | **str** | Category description | [optional] [default to '']
**button_image_url** | **str** | Link to image | [optional] 
**header_image_url** | **str** |  | [optional] 
**iiko_group_id** | **str** | iikoGroupId | [optional] 
**items** | [**List[ExternalMenuItem]**](ExternalMenuItem.md) |  | 
**schedule_id** | **str** | Category schedule GUID | [optional] 
**schedule_name** | **str** | Category schedule name | [optional] 
**schedules** | [**List[PeriodScheduleDto]**](PeriodScheduleDto.md) | Category schedule intervals | [optional] 
**is_hidden** | **bool** | Visibility flag | [optional] [default to False]
**tags** | [**List[TagDto]**](TagDto.md) |  | [optional] 
**labels** | [**List[LabelDto]**](LabelDto.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_category import ExternalMenuCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuCategory from a JSON string
external_menu_category_instance = ExternalMenuCategory.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuCategory.to_json())

# convert the object into a dict
external_menu_category_dict = external_menu_category_instance.to_dict()
# create an instance of ExternalMenuCategory from a dict
external_menu_category_from_dict = ExternalMenuCategory.from_dict(external_menu_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


