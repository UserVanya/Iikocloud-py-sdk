# WebHookShortFilter

Filter for updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | **bool** | Flag for updates. | [optional] 

## Example

```python
from iikocloud_client.models.web_hook_short_filter import WebHookShortFilter

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookShortFilter from a JSON string
web_hook_short_filter_instance = WebHookShortFilter.from_json(json)
# print the JSON string representation of the object
print(WebHookShortFilter.to_json())

# convert the object into a dict
web_hook_short_filter_dict = web_hook_short_filter_instance.to_dict()
# create an instance of WebHookShortFilter from a dict
web_hook_short_filter_from_dict = WebHookShortFilter.from_dict(web_hook_short_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


