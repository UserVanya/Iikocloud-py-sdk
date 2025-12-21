# ExternalMenuCategory2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category ID | [optional] 
**name** | **str** | Category name | [optional] [default to '']
**description** | **str** | Category description | [optional] [default to '']
**button_image_url** | **str** | Link to image | [optional] 
**iiko_group_id** | **str** | iikoGroupId | [optional] 
**items** | [**List[ExternalMenuItem2]**](ExternalMenuItem2.md) |  | 
**schedule_id** | **str** | Category schedule GUID | [optional] 
**schedule_name** | **str** | Category schedule name | [optional] 
**schedules** | [**List[PeriodScheduleDto2]**](PeriodScheduleDto2.md) | Category schedule intervals | [optional] 
**is_hidden** | **bool** | Visibility flag | [optional] [default to False]
**labels** | **List[str]** | List of labels | [optional] 
**tags** | **List[str]** | List of tags | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_category2 import ExternalMenuCategory2

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuCategory2 from a JSON string
external_menu_category2_instance = ExternalMenuCategory2.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuCategory2.to_json())

# convert the object into a dict
external_menu_category2_dict = external_menu_category2_instance.to_dict()
# create an instance of ExternalMenuCategory2 from a dict
external_menu_category2_from_dict = ExternalMenuCategory2.from_dict(external_menu_category2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


