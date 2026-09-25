# MenuV3CustomerTagGroup

Customer tag group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tag group ID. | 
**items** | [**List[TagItem]**](TagItem.md) | List of tags. | [optional] 
**name** | **str** | Tag group name. | 
**select_several_tags** | **bool** | Flag indicating whether multiple tags can be selected. | [optional] 

## Example

```python
from iikocloud_client.models.menu_v3_customer_tag_group import MenuV3CustomerTagGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3CustomerTagGroup from a JSON string
menu_v3_customer_tag_group_instance = MenuV3CustomerTagGroup.from_json(json)
# print the JSON string representation of the object
print(MenuV3CustomerTagGroup.to_json())

# convert the object into a dict
menu_v3_customer_tag_group_dict = menu_v3_customer_tag_group_instance.to_dict()
# create an instance of MenuV3CustomerTagGroup from a dict
menu_v3_customer_tag_group_from_dict = MenuV3CustomerTagGroup.from_dict(menu_v3_customer_tag_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


