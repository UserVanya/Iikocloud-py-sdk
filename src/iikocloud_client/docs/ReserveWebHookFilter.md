# ReserveWebHookFilter

Filter for updates and errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **bool** | Flag for errors. | [optional] 
**updates** | **bool** | Flag for updates. | [optional] 

## Example

```python
from iikocloud_client.models.reserve_web_hook_filter import ReserveWebHookFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveWebHookFilter from a JSON string
reserve_web_hook_filter_instance = ReserveWebHookFilter.from_json(json)
# print the JSON string representation of the object
print(ReserveWebHookFilter.to_json())

# convert the object into a dict
reserve_web_hook_filter_dict = reserve_web_hook_filter_instance.to_dict()
# create an instance of ReserveWebHookFilter from a dict
reserve_web_hook_filter_from_dict = ReserveWebHookFilter.from_dict(reserve_web_hook_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


