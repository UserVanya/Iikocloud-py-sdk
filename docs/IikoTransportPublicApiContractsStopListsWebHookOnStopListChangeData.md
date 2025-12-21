# IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData

Out-of-stock list update info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_groups_stop_lists_updates** | [**List[IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate]**](IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate.md) | Terminal groups with out-of-stock list updates. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_web_hook_on_stop_list_change_data import IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData from a JSON string
iiko_transport_public_api_contracts_stop_lists_web_hook_on_stop_list_change_data_instance = IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_web_hook_on_stop_list_change_data_dict = iiko_transport_public_api_contracts_stop_lists_web_hook_on_stop_list_change_data_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData from a dict
iiko_transport_public_api_contracts_stop_lists_web_hook_on_stop_list_change_data_from_dict = IikoTransportPublicApiContractsStopListsWebHookOnStopListChangeData.from_dict(iiko_transport_public_api_contracts_stop_lists_web_hook_on_stop_list_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


