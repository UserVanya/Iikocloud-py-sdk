# RmsItemsResponseWrapperStopListsTerminalGroupStopList

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsStopListsTerminalGroupStopList]**](IikoTransportPublicApiContractsStopListsTerminalGroupStopList.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.rms_items_response_wrapper_stop_lists_terminal_group_stop_list import RmsItemsResponseWrapperStopListsTerminalGroupStopList

# TODO update the JSON string below
json = "{}"
# create an instance of RmsItemsResponseWrapperStopListsTerminalGroupStopList from a JSON string
rms_items_response_wrapper_stop_lists_terminal_group_stop_list_instance = RmsItemsResponseWrapperStopListsTerminalGroupStopList.from_json(json)
# print the JSON string representation of the object
print(RmsItemsResponseWrapperStopListsTerminalGroupStopList.to_json())

# convert the object into a dict
rms_items_response_wrapper_stop_lists_terminal_group_stop_list_dict = rms_items_response_wrapper_stop_lists_terminal_group_stop_list_instance.to_dict()
# create an instance of RmsItemsResponseWrapperStopListsTerminalGroupStopList from a dict
rms_items_response_wrapper_stop_lists_terminal_group_stop_list_from_dict = RmsItemsResponseWrapperStopListsTerminalGroupStopList.from_dict(rms_items_response_wrapper_stop_lists_terminal_group_stop_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


