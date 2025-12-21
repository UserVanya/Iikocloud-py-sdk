# IikoTransportPublicApiContractsWebHooksStopListUpdateWebHookEventInfo

WebHook notification about stop list update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringStopListUpdate**](ConstantStringStopListUpdate.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData**](IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_stop_list_update_web_hook_event_info import IikoTransportPublicApiContractsWebHooksStopListUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsWebHooksStopListUpdateWebHookEventInfo from a JSON string
iiko_transport_public_api_contracts_web_hooks_stop_list_update_web_hook_event_info_instance = IikoTransportPublicApiContractsWebHooksStopListUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsWebHooksStopListUpdateWebHookEventInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_web_hooks_stop_list_update_web_hook_event_info_dict = iiko_transport_public_api_contracts_web_hooks_stop_list_update_web_hook_event_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsWebHooksStopListUpdateWebHookEventInfo from a dict
iiko_transport_public_api_contracts_web_hooks_stop_list_update_web_hook_event_info_from_dict = IikoTransportPublicApiContractsWebHooksStopListUpdateWebHookEventInfo.from_dict(iiko_transport_public_api_contracts_web_hooks_stop_list_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


