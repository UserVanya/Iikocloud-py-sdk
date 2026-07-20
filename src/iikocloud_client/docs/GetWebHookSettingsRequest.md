# GetWebHookSettingsRequest

Request to get webhooks settings for specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization UOC Id.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_web_hook_settings_request import GetWebHookSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebHookSettingsRequest from a JSON string
get_web_hook_settings_request_instance = GetWebHookSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(GetWebHookSettingsRequest.to_json())

# convert the object into a dict
get_web_hook_settings_request_dict = get_web_hook_settings_request_instance.to_dict()
# create an instance of GetWebHookSettingsRequest from a dict
get_web_hook_settings_request_from_dict = GetWebHookSettingsRequest.from_dict(get_web_hook_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


