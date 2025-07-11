# TransportCommonRmsItemsResponseWrapperTerminalGroupStopList

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportStopListsTerminalGroupStopList]**](TransportStopListsTerminalGroupStopList.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.transport_common_rms_items_response_wrapper_terminal_group_stop_list import TransportCommonRmsItemsResponseWrapperTerminalGroupStopList

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonRmsItemsResponseWrapperTerminalGroupStopList from a JSON string
transport_common_rms_items_response_wrapper_terminal_group_stop_list_instance = TransportCommonRmsItemsResponseWrapperTerminalGroupStopList.from_json(json)
# print the JSON string representation of the object
print(TransportCommonRmsItemsResponseWrapperTerminalGroupStopList.to_json())

# convert the object into a dict
transport_common_rms_items_response_wrapper_terminal_group_stop_list_dict = transport_common_rms_items_response_wrapper_terminal_group_stop_list_instance.to_dict()
# create an instance of TransportCommonRmsItemsResponseWrapperTerminalGroupStopList from a dict
transport_common_rms_items_response_wrapper_terminal_group_stop_list_from_dict = TransportCommonRmsItemsResponseWrapperTerminalGroupStopList.from_dict(transport_common_rms_items_response_wrapper_terminal_group_stop_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


