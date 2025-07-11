# ExternalMenuPreset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the external menu | [optional] 
**name** | **str** | External menu name | [optional] 
**description** | **str** | External menu description | [optional] 
**item_categories** | [**List[TransportMenuCategoryDto]**](TransportMenuCategoryDto.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_preset import ExternalMenuPreset

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuPreset from a JSON string
external_menu_preset_instance = ExternalMenuPreset.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuPreset.to_json())

# convert the object into a dict
external_menu_preset_dict = external_menu_preset_instance.to_dict()
# create an instance of ExternalMenuPreset from a dict
external_menu_preset_from_dict = ExternalMenuPreset.from_dict(external_menu_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


