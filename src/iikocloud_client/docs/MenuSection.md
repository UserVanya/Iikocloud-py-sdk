# MenuSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.menu_section import MenuSection

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSection from a JSON string
menu_section_instance = MenuSection.from_json(json)
# print the JSON string representation of the object
print(MenuSection.to_json())

# convert the object into a dict
menu_section_dict = menu_section_instance.to_dict()
# create an instance of MenuSection from a dict
menu_section_from_dict = MenuSection.from_dict(menu_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


