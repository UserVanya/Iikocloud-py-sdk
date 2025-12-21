# IikoTransportPublicApiContractsWebHooksTableOrderUpdateWebHookEventInfo

WebHook notification about table order update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringTableOrderUpdate**](ConstantStringTableOrderUpdate.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo**](IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_table_order_update_web_hook_event_info import IikoTransportPublicApiContractsWebHooksTableOrderUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsWebHooksTableOrderUpdateWebHookEventInfo from a JSON string
iiko_transport_public_api_contracts_web_hooks_table_order_update_web_hook_event_info_instance = IikoTransportPublicApiContractsWebHooksTableOrderUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsWebHooksTableOrderUpdateWebHookEventInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_web_hooks_table_order_update_web_hook_event_info_dict = iiko_transport_public_api_contracts_web_hooks_table_order_update_web_hook_event_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsWebHooksTableOrderUpdateWebHookEventInfo from a dict
iiko_transport_public_api_contracts_web_hooks_table_order_update_web_hook_event_info_from_dict = IikoTransportPublicApiContractsWebHooksTableOrderUpdateWebHookEventInfo.from_dict(iiko_transport_public_api_contracts_web_hooks_table_order_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


