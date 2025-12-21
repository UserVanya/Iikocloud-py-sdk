# ExternalMenuComboItemSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Size name | 
**size_id** | **str** | Size GUID | 
**short_name** | **str** | Short size name | [optional] [default to '']
**is_hidden** | **bool** | Visibility flag | [optional] [default to False]
**button_image_url** | **str** | Link to image | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_combo_item_size import ExternalMenuComboItemSize

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuComboItemSize from a JSON string
external_menu_combo_item_size_instance = ExternalMenuComboItemSize.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuComboItemSize.to_json())

# convert the object into a dict
external_menu_combo_item_size_dict = external_menu_combo_item_size_instance.to_dict()
# create an instance of ExternalMenuComboItemSize from a dict
external_menu_combo_item_size_from_dict = ExternalMenuComboItemSize.from_dict(external_menu_combo_item_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


