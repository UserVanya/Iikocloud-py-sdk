# IikoTransportPublicApiContractsWebHooksDeliveryOrderErrorWebHookEventInfo

WebHook notification about delivery order saving error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringDeliveryOrderError**](ConstantStringDeliveryOrderError.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_delivery_order_error_web_hook_event_info import IikoTransportPublicApiContractsWebHooksDeliveryOrderErrorWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsWebHooksDeliveryOrderErrorWebHookEventInfo from a JSON string
iiko_transport_public_api_contracts_web_hooks_delivery_order_error_web_hook_event_info_instance = IikoTransportPublicApiContractsWebHooksDeliveryOrderErrorWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsWebHooksDeliveryOrderErrorWebHookEventInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_web_hooks_delivery_order_error_web_hook_event_info_dict = iiko_transport_public_api_contracts_web_hooks_delivery_order_error_web_hook_event_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsWebHooksDeliveryOrderErrorWebHookEventInfo from a dict
iiko_transport_public_api_contracts_web_hooks_delivery_order_error_web_hook_event_info_from_dict = IikoTransportPublicApiContractsWebHooksDeliveryOrderErrorWebHookEventInfo.from_dict(iiko_transport_public_api_contracts_web_hooks_delivery_order_error_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


