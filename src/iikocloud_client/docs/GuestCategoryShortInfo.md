# GuestCategoryShortInfo

Guest category info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Category id. | [optional] 
**is_active** | **bool** | Is category active or not. | [optional] 
**is_default_for_new_guests** | **bool** | Is category default for new guests or not. | [optional] 
**name** | **str** | Category name. | [optional] 

## Example

```python
from iikocloud_client.models.guest_category_short_info import GuestCategoryShortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestCategoryShortInfo from a JSON string
guest_category_short_info_instance = GuestCategoryShortInfo.from_json(json)
# print the JSON string representation of the object
print(GuestCategoryShortInfo.to_json())

# convert the object into a dict
guest_category_short_info_dict = guest_category_short_info_instance.to_dict()
# create an instance of GuestCategoryShortInfo from a dict
guest_category_short_info_from_dict = GuestCategoryShortInfo.from_dict(guest_category_short_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


