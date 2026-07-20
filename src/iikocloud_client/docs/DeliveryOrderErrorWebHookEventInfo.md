# DeliveryOrderErrorWebHookEventInfo

WebHook notification about delivery order saving error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**OrderInfo**](OrderInfo.md) | Event details. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**event_type** | **str** | Event type. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_error_web_hook_event_info import DeliveryOrderErrorWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderErrorWebHookEventInfo from a JSON string
delivery_order_error_web_hook_event_info_instance = DeliveryOrderErrorWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderErrorWebHookEventInfo.to_json())

# convert the object into a dict
delivery_order_error_web_hook_event_info_dict = delivery_order_error_web_hook_event_info_instance.to_dict()
# create an instance of DeliveryOrderErrorWebHookEventInfo from a dict
delivery_order_error_web_hook_event_info_from_dict = DeliveryOrderErrorWebHookEventInfo.from_dict(delivery_order_error_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


