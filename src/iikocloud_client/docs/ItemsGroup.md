# ItemsGroup

Item group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_image_url** | **str** | Button image URL. | [optional] 
**description** | **str** | Group description. | [optional] 
**id** | **str** | Group ID. | 
**image** | [**Image**](Image.md) | Group image. Replaces ButtonImageUrl. | [optional] 
**is_hidden** | **bool** | Flag indicating whether the group is hidden. | [optional] 
**items** | [**List[Item]**](Item.md) | List of items in the group. | [optional] 
**labels** | **List[str]** | List of website tags associated with the element. | [optional] 
**name** | **str** | Group name. | 
**schedule_id** | **str** | Schedule ID. | [optional] 
**tags** | **List[str]** | List of internal tags associated with the element. | [optional] 

## Example

```python
from iikocloud_client.models.items_group import ItemsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsGroup from a JSON string
items_group_instance = ItemsGroup.from_json(json)
# print the JSON string representation of the object
print(ItemsGroup.to_json())

# convert the object into a dict
items_group_dict = items_group_instance.to_dict()
# create an instance of ItemsGroup from a dict
items_group_from_dict = ItemsGroup.from_dict(items_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


