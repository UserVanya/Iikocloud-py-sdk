# ExternalMenu

External menu, related to ApiLogin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.external_menu import ExternalMenu

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenu from a JSON string
external_menu_instance = ExternalMenu.from_json(json)
# print the JSON string representation of the object
print(ExternalMenu.to_json())

# convert the object into a dict
external_menu_dict = external_menu_instance.to_dict()
# create an instance of ExternalMenu from a dict
external_menu_from_dict = ExternalMenu.from_dict(external_menu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


