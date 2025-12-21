# WebHooksTableOrderUpdateWebHookEventInfo

WebHook notification about table order update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringTableOrderUpdate**](ConstantStringTableOrderUpdate.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**TableOrdersResponseTableOrderInfo**](TableOrdersResponseTableOrderInfo.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.web_hooks_table_order_update_web_hook_event_info import WebHooksTableOrderUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksTableOrderUpdateWebHookEventInfo from a JSON string
web_hooks_table_order_update_web_hook_event_info_instance = WebHooksTableOrderUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(WebHooksTableOrderUpdateWebHookEventInfo.to_json())

# convert the object into a dict
web_hooks_table_order_update_web_hook_event_info_dict = web_hooks_table_order_update_web_hook_event_info_instance.to_dict()
# create an instance of WebHooksTableOrderUpdateWebHookEventInfo from a dict
web_hooks_table_order_update_web_hook_event_info_from_dict = WebHooksTableOrderUpdateWebHookEventInfo.from_dict(web_hooks_table_order_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


