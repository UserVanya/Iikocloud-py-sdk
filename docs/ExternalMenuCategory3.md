# ExternalMenuCategory3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category ID | [optional] 
**name** | **str** | Category name | [optional] [default to '']
**description** | **str** | Category description | [optional] [default to '']
**button_image_url** | **str** | Link to image | [optional] 
**iiko_group_id** | **str** | iikoGroupId | [optional] 
**schedule_id** | **str** | Category schedule GUID | [optional] 
**schedule_name** | **str** | Category schedule name | [optional] 
**schedules** | [**List[PeriodScheduleDto3]**](PeriodScheduleDto3.md) | Category schedule intervals | [optional] 
**is_hidden** | **bool** | Visibility flag | [optional] [default to False]
**items** | [**List[ExternalMenuCategory3ItemsInner]**](ExternalMenuCategory3ItemsInner.md) |  | 
**labels** | **List[str]** | List of labels | [optional] 
**tags** | **List[str]** | List of tags | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_category3 import ExternalMenuCategory3

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuCategory3 from a JSON string
external_menu_category3_instance = ExternalMenuCategory3.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuCategory3.to_json())

# convert the object into a dict
external_menu_category3_dict = external_menu_category3_instance.to_dict()
# create an instance of ExternalMenuCategory3 from a dict
external_menu_category3_from_dict = ExternalMenuCategory3.from_dict(external_menu_category3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


