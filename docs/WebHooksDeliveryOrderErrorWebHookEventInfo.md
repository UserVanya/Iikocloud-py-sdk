# WebHooksDeliveryOrderErrorWebHookEventInfo

WebHook notification about delivery order saving error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringDeliveryOrderError**](ConstantStringDeliveryOrderError.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**DeliveriesResponseOrderOrderInfo**](DeliveriesResponseOrderOrderInfo.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.web_hooks_delivery_order_error_web_hook_event_info import WebHooksDeliveryOrderErrorWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksDeliveryOrderErrorWebHookEventInfo from a JSON string
web_hooks_delivery_order_error_web_hook_event_info_instance = WebHooksDeliveryOrderErrorWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(WebHooksDeliveryOrderErrorWebHookEventInfo.to_json())

# convert the object into a dict
web_hooks_delivery_order_error_web_hook_event_info_dict = web_hooks_delivery_order_error_web_hook_event_info_instance.to_dict()
# create an instance of WebHooksDeliveryOrderErrorWebHookEventInfo from a dict
web_hooks_delivery_order_error_web_hook_event_info_from_dict = WebHooksDeliveryOrderErrorWebHookEventInfo.from_dict(web_hooks_delivery_order_error_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


