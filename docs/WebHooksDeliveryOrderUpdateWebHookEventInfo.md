# WebHooksDeliveryOrderUpdateWebHookEventInfo

WebHook notification about delivery order update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringDeliveryOrderUpdate**](ConstantStringDeliveryOrderUpdate.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**correlation_id** | **str** | Operation ID. | [optional] 
**event_info** | [**DeliveriesResponseOrderOrderInfo**](DeliveriesResponseOrderOrderInfo.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.web_hooks_delivery_order_update_web_hook_event_info import WebHooksDeliveryOrderUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksDeliveryOrderUpdateWebHookEventInfo from a JSON string
web_hooks_delivery_order_update_web_hook_event_info_instance = WebHooksDeliveryOrderUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(WebHooksDeliveryOrderUpdateWebHookEventInfo.to_json())

# convert the object into a dict
web_hooks_delivery_order_update_web_hook_event_info_dict = web_hooks_delivery_order_update_web_hook_event_info_instance.to_dict()
# create an instance of WebHooksDeliveryOrderUpdateWebHookEventInfo from a dict
web_hooks_delivery_order_update_web_hook_event_info_from_dict = WebHooksDeliveryOrderUpdateWebHookEventInfo.from_dict(web_hooks_delivery_order_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


